import json
from django.apps import apps
from django.db.models import Avg, Sum, Max, Min, Count

from i2amparis_main.models import Dataset
from data_manager.models import Query

from django.db.models import Q

from visualiser.visualiser_settings import DATA_TABLES_APP


def query_execute(query_id):
    '''
    This method is responsible for executing a query using Django's ORM. Calling selecting, filtering, grouping,
    ordering functions.
    :param query_id: The id of the query to be executed
    :return: The data returned by the executed query.
    '''
    dataset, select, filters, ordering, grouping, add_params = get_query_parameters(query_id)
    dataset = Dataset.objects.get(dataset_name=dataset)
    data_model = apps.get_model(DATA_TABLES_APP, dataset.dataset_django_model)
    filter_list = extract_filters(filters)
    order_list = extract_orderings(ordering)
    group_by_params, agg_params = extract_groupings(grouping)
    if (len(grouping['params']) == 0) and (len(grouping['aggregated_params']) == 0):
        select_data = data_model.objects.only(*select).filter(filter_list).order_by(*order_list).values(*select)
    else:
        filtered_data = data_model.objects.filter(filter_list)
        grouped_by_data = group_by_function(group_by_params, agg_params, filtered_data)
        select_data = grouped_by_data.order_by(
            *order_list)
    print(filter_list)
    return select_data, add_params



def extract_orderings(ordering):
    '''
    This method converts the JSON format ordering to a compatible list for Django ORM
    :param ordering: Dictionary Array
    :return: list of strings
    '''
    ordering_list = []
    for el in ordering:
        if el['ascending'] is True:
            ordering_list.append(el['parameter'])
        else:
            ordering_list.append("-" + el['parameter'])
    return ordering_list


def extract_groupings(grouping):
    '''
    This method converts the JSON format grouping to 2 compatible lists for the Django ORM
    :param grouping: Dictionary
    :return: 1 list of strings and 1 dictionary
    '''
    group_by_params = grouping['params']
    agg_params = {}
    for el in grouping['aggregated_params']:
        agg_params[el['name']] = str(el['agg_func'])
    return group_by_params, agg_params


def group_by_function(group_by_params, agg_params, data):
    '''This method applies the aggregate functions to the grouped data
    :param group_by_params: The parameters according to which the grouping takes place
    :param agg_params: The parameters that are aggregated according to the given aggregate function
    :param data: The data loaded to the method'''
    final_data = data.values(*group_by_params)
    for value, agg_func in agg_params.items():
        if agg_func == 'Avg':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Avg'))
        elif agg_func == 'Sum':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Sum'))
        elif agg_func == 'Max':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Max'))
        elif agg_func == 'Min':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Min'))
        elif agg_func == 'Count':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Count'))
        elif agg_func == 'default':
            final_data = final_data.annotate(**get_groupby_annotation(value, 'Avg'))
    return final_data


def get_groupby_annotation(value, agg_func):
    '''Creates a dictionary used for the group by annotation used in the grouping methods.'''
    if agg_func == 'Avg':
        return {value: Avg(value)}
    elif agg_func == 'Sum':
        return {value: Sum(value)}
    elif agg_func == 'Max':
        return {value: Max(value)}
    elif agg_func == 'Min':
        return {value: Min(value)}
    elif agg_func == 'Count':
        return {value:Count(value)}

def get_query_parameters(query_id):
    '''
    This method is used for retrieving all the necessary parameters of the query
    :param query_id: The query_id whose parameters are extracted
    :return: A JSON object containing all query parameters
    '''
    query = Query.objects.get(id=query_id)
    parameters = query.parameters
    q_params = json.loads(parameters.replace('\r\n', ''))
    dataset = q_params['dataset']
    select = q_params['query_configuration']['select']
    filters = q_params['query_configuration']['filter']
    ordering = q_params['query_configuration']['ordering']
    grouping = q_params['query_configuration']['grouping']
    add_params = q_params['additional_app_parameters']
    return dataset, select, filters, ordering, grouping, add_params


def extract_filters(filters):
    '''This method calls functions for creating the orm expressions for filtering the data'''
    #TODO: A new method for more complex filtering should be developed
    exp_and = compute_Q_objects(filters['and'], 'and')
    print("and expr=", exp_and)
    exp_or = compute_Q_objects(filters['or'], 'or')
    print("or expr=", exp_or)
    return exp_and & exp_or


def compute_dict(d):
    '''This method applies the specific filtering according to given operands'''
    q_dict = {}
    if d['operation'] == ">":
        q_dict = {str(d['operand_1']) + '__' + 'gt': str(d['operand_2'])}
    elif d['operation'] == ">=":
        q_dict = {str(d['operand_1']) + '__' + 'gte': str(d['operand_2'])}
    elif d['operation'] == "<":
        q_dict = {str(d['operand_1']) + '__' + 'lt': str(d['operand_2'])}
    elif d['operation'] == "<=":
        q_dict = {str(d['operand_1']) + '__' + 'lte': str(d['operand_2'])}
    elif d['operation'] == "between":
        q_dict1 = {str(d['operand_1']) + '__' + 'lte': str(d['operand_2'][1])}
        q_dict2 = {str(d['operand_1']) + '__' + 'gte': str(d['operand_2'][0])}
        q_dict = {q_dict1, q_dict2}
    elif d['operation'] == "=":
        q_dict = {str(d['operand_1']): str(d['operand_2'])}
    elif d['operation'] == "in":
        q_dict = {str(d['operand_1']) + '__' + 'in': d['operand_2']}
    expr = (Q(**q_dict))
    return expr


def compute_Q_objects(param, op):
    '''This functions creates the ORM filtering expressios'''
    q_objects = Q()
    for item in param:
        if op == 'and':
            q_objects &= compute_dict(item)
        else:
            q_objects |= compute_dict(item)
    return q_objects

# Functions used by the ORM Manager
def clean_dictionary_list_from_zero_values(list):
    '''This method clears the data from falsely inserted zeros in the database'''
    clean_final_data = []
    for el in list:
        clean_final_data.append({x: y for x, y in el.items() if y != 0})
    return clean_final_data


def clean_dictionary_list_from_null_values(list):
    '''This method clears the data from null values created in the dataframes by pivoting'''
    clean_final_data = []
    for el in list:
        clean_final_data.append({x: y for x, y in el.items() if y != -999999})
    return clean_final_data

