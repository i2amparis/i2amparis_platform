from django.apps import apps
import ast
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import sys
from django.views.decorators.clickjacking import xframe_options_exempt

from data_manager.orm_query_manager import heatmap_query, line_chart_query, column_chart_query, \
    pie_chart_query

from i2amparis_main.models import Harmonisation_Variables, Variable, Dataset
from visualiser.visualiser_settings import DATA_TABLES_APP

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)

# TODO: We need to make AM_CHARTS_COLOR_CODES_LIST more consistent. Suggestion: lighter_color,light_color,color,
#  dark_color, darker_color.

# COLORS OF THE VISUALISATION ENGINE

AM_CHARTS_COLOR_INDEX_LIST = {
    "light_blue": 0,
    "blue": 1,
    "violet_blue": 2,
    "purple": 4,
    "fuchsia": 7,
    "red": 8,
    "ceramic": 9,
    "light_brown": 10,
    "mustard": 11,
    "light_green": 13,
    "green": 16,
    "cyan": 19,
}

AM_CHARTS_COLOR_CODES_LIST = {
    "lighter_blue": "#9ec5e8",
    "light_blue": "#5B9BD5",
    "moody_blue": "#487caa",
    "dark_blue": "#2d4d6a",
    "ocean_dark_blue": "#1f4e79",
    "blue": "#5079d4",
    "petrol_blue": "#066f7c",
    "violet": "#a78ccf",
    "purple": "#7d3e9d",
    "fuchsia": "#a04293",
    "light_red": "#e15b64",
    "red": "#ad3741",
    "ceramic": "#a0432c",
    "orange_red": "#f47e60",
    "orange": "#ff950b",
    "orange_fire": "#c55a11",
    "light_brown": "#844b2c",
    "brown": "#634b3e",
    "calm_brown": "#b0866f",
    "yellow": "#efd453",
    "orange_yellow": "#f8b26a",
    "mustard": "#a78428",
    "gold": "#e6b323",
    "lighter_green": "#a8cc91",
    "light_green": "#62993d",
    "green": "#4a8540",
    "casual_green": "#568637",
    "grey_green": "#abbd81",
    "oil_green": "#839627",
    "cyan": "#4b9e91",
    "black": "#000000",
    "gray": "#999999",
    "dark_gray": "#3a3b3c",
    "ice_gray": "#d8e5eb",
    "white": "#FFFFFF",
    "light_cyan": "#bfe1e7",
    "dark_green": "#314a15",
    "lighter_grey": "#c0cea1",
    "deep_red": "#8b0304",
    "open_green": "#94b663",
    "green_new": "#31a354",
    "green_open_new": "#addd8e",
    "yellow_open_new": "#f7fcb9",
    "orange_new": "#fdc086",
    "purple_new": "#beaed4"

}

AM_CHARTS_COLOR_HEATMAP_COUPLES = {
    "blue_red": ["#63a1db", "#a32f22"],
    "green_red": ["#66bd7d", "#a32f22"],
    "beige_purple": ["#f0d2bd", "#80308a"],
    "purple_orange": ["#f5d1ff", "#db6b21"],
    "cyan_green": ["#d5eded", "#446614"],
    "yellow_gold": ["#f7ecc2", "#dba200"],
    "skin_red": ["#f7dfd0", "#8d1915"],
    "grey_darkblue": ["#eaecf7", "#1f3b5e"],
    "lightblue_green": ["#bbe1ff", "#2e5c20"],
    "darkblue_lightgreen": ["#02487a", "#8cc63f"]

}

# SCIENTIFIC INTERFACE SPECIFIC COLOR MAPPING
COLOR_MODELS = {
    "42": "moody_blue",
    "eu_times": "cyan",
    "e3me": "light_red",
    "gcam": "orange_fire",
    "gemini_e3": "grey_green",
    "ices": "light_brown",
    "muse": "gold",
    "nemesis": "ice_gray",
    "tiam": "purple"
}

SCENARIOS_LINE_TYPES = {
    "Baseline": "0,0",
    "CP_EI": "1,1",
    "NDC_EI": "3,3",
    "NDC_LTT": "4,2",
    "PR_CurPol_CP": "0,0",
    "PR_CurPol_EI": "1,1",
    "PR_CurPol_CPO": "4,2",
    "PR_NDC_CP": "3,3",
    "PR_NDC_EI": "2,5",
    "PR_NDC_CPO": "1,6",
    "PR_Baseline": "1,6",
    "Unharmonised baseline": "0,0",
    "EUWWH": "0,0",
    "WWH": "0,0",
    "NZE": "3,3",
}


def define_color_index_list(color_list_request):
    color_list = []
    for color in color_list_request:
        color_list.append(AM_CHARTS_COLOR_INDEX_LIST[color])
    return color_list


def define_color_code_list(color_list_request):
    color_list = []
    for color in color_list_request:
        if not AM_CHARTS_COLOR_CODES_LIST.get(color) is None:
            color_list.append(AM_CHARTS_COLOR_CODES_LIST[color])
    return color_list


# LOADING VISUALIZATION PARAMETERS FROM REQUEST

@csrf_exempt
def get_response_data_XY(request):
    '''
    This method retrieves all the parameters from the request
    :return: A JSON object containing all request parameters for the visualisation
    '''
    if request.method == "GET":
        json_response = {
            "y_var_names": request.GET.getlist("y_var_names[]", []),
            "y_var_titles": request.GET.getlist("y_var_titles[]", []),
            "y_var_units": request.GET.getlist("y_var_units[]", []),
            "x_axis_type": request.GET.get("x_axis_type", ""),
            "x_axis_name": request.GET.get("x_axis_name", ""),
            "x_axis_title": request.GET.get("x_axis_title", ""),
            "x_axis_unit": request.GET.get("x_axis_unit", ""),
            "x_sec_axis": request.GET.get("x_sec_axis", ""),
            "y_axis_title": request.GET.get("y_axis_title", ""),
            "color_list_request": request.GET.getlist("color_list_request[]", []),
            "use_default_colors": request.GET.get("use_default_colors", "true"),
            "chart_3d": request.GET.get("chart_3d", "false"),
            "legend_position": request.GET.get("legend_position", "bottom"),
            "min_max_y_value": request.GET.getlist("min_max_y_value[]", []),
            "dataset": request.GET.get("dataset", ""),
            "dataset_type": request.GET.get("dataset_type", "file"),
            "distinct": request.GET.getlist("distinct[]", []),
            "stacked": request.GET.get("stacked", "false"),
            "ranges": request.GET.getlist("ranges[]", []),
            "markers_on_chart": request.GET.get("markers_on_chart", "true"),
            "line_type_list": request.GET.getlist("line_type_list[]", []),
            "view_legend": request.GET.get("view_legend", "true"),

        }
    else:
        json_response = json.loads(request.body.decode('utf-8'))
    return json_response


@csrf_exempt
def get_response_heat_map(request):
    '''
    This method retrieves all the addition parameters necessary for the heatmap visualisation
    :return: A JSON object with all the necessary parameters
    '''
    if request.method == "GET":
        json_response = {
            "z_axis_name": request.GET.get("z_axis_name", ""),
            "z_axis_title": request.GET.get("z_axis_title", ""),
            "z_axis_unit": request.GET.get("z_axis_unit", ""),
            "min_max_z_value": request.GET.getlist("min_max_z_value[]", []),
        }
    else:
        json_response = json.loads(request.body)
        print(json_response)
    return json_response


@csrf_exempt
def get_response_heat_map_on_map(request):
    if request.method == "GET":
        json_response = {
            "projection": request.GET.get("projection", ""),
            "map_var_name": request.GET.get("map_var_name", ""),
            "map_var_title": request.GET.get("map_var_title", ""),
            "map_var_unit": request.GET.get("map_var_unit", "")
        }
    else:
        json_response = json.loads(request.body)
        print(json_response)
    return json_response


@csrf_exempt
def get_response_flow_diagram(request):
    if request.method == "GET":
        json_response = {
            "use_def_colors": request.GET.get("use_def_colors", "false"),
            "chart_title": request.GET.get("chart_title", ""),
            "node_list": request.GET.getlist("node_list[]", []),
            "color_node_list": request.GET.getlist("color_node_list[]", []),
        }
    else:
        json_response = json.loads(request.body)
        print(json_response)
    return json_response


@csrf_exempt
@xframe_options_exempt
def get_response_parallel_coordinates_chart(request):
    if request.method == "GET":
        json_response = {
            "y_axes": request.GET.getlist("y_axes[]", []),
            "title": request.GET.get("title", ""),
            "about_title": request.GET.get("title", ""),
            "about_text": request.GET.get("text", ""),
            "groups_title": request.GET.get("groups_title", ""),
            "samples_size": request.GET.get("samples_size", "10"),

        }
    else:
        json_response = json.loads(request.body)
        print(json_response)
    return json_response


# DATA GENERATORS METHODS
# The visualiser uses files, existing whole data tables in the db or calls the Data Manager to retrieve data.
# Not all methods are implemented for every visualisation

# DATA CREATION METHOD SELECTORS
@csrf_exempt
def generate_data_for_line_chart(dataset, dataset_type):
    final_data = []
    if dataset_type == 'file':
        final_data = line_chart_data_from_file('visualiser/fake_data/' + dataset)
        print('Retrieved data from file')
    elif dataset_type == 'db':
        dataset = Dataset.objects.get(dataset_name=dataset)
        data_table = apps.get_model(DATA_TABLES_APP, dataset.dataset_django_model)
        data = data_table.objects.all()
        variables = Variable.objects.filter(dataset_relation=dataset.id).order_by('id')
        final_data = reformat_chart_data(data, variables)
    elif dataset_type == 'query':
        final_data = line_chart_query(dataset)

    return final_data


@csrf_exempt
def generate_data_for_column_chart(dataset, dataset_type):
    final_data = []
    if dataset_type == 'query':
        final_data = column_chart_query(dataset)
    return final_data


@csrf_exempt
def generate_data_for_pie_chart(dataset, dataset_type):
    final_data = []
    if dataset_type == 'query':
        final_data = pie_chart_query(dataset)
    return final_data


def create_stacked_clustered_data(dataset, dataset_type):
    final_data = []
    if dataset_type == 'query':
        final_data = column_chart_query(dataset)
    elif dataset_type == 'dataframe':
        pass
    return final_data


# FILE READING METHODS
@csrf_exempt
def line_chart_data_from_file(dataset):
    with open(dataset) as f:
        final_data = ast.literal_eval(f.read())
    return final_data


def heatmap_chart_data_from_file(dataset):
    '''
    This method is used for reading data from a file
    :param dataset: the name(path) of a file that is going to be used
    :return: Data in a suitable format for the heatmap chart
    '''
    final_data = []
    with open('static/harmonisation_data/' + dataset, 'r') as f:
        data = f.read()
    diction = json.loads(data)
    for model, vars in diction.items():
        for var, val in vars.items():
            var_title = Harmonisation_Variables.objects.get(var_name=var).var_title
            final_data.append({"model": model, "variable": var_title, "value": val})
    print(final_data)
    return final_data


# ORM Data Creation Methods. (Currently only used for heatmap)
def create_heatmap_data(dataset, row_categorisation_dataset, col_categorisation_dataset, col_order, row_order,
                        dataset_type, workspace):
    '''
    This method contains all the ways for creating a heatmap chart using data from a file, a whole table in the database, a query or a dataframe.
    :param dataset: the name of the file in case dataset_type = "file", the name of the table if dataset_type = "db", the id of the query if dataset_type = "query"
    :param row_categorisation_dataset, col_categorisation_dataset: these parameters are used for categorising the variables in the x and y axis of the heatmap according to a given data_set
    :param col_order, row_order: these parameters are used for ordering the elements of the rows and columns of the heatmap according to a given variable
    :param dataset_type: values: "db", "file", "dataframe", query
    :return: the necessary data for the creation of the heatmap chart in the suitable format
    '''
    final_data = []
    row_ranges_data = []
    col_ranges_data = []
    if dataset_type == 'file':
        final_data = heatmap_chart_data_from_file(dataset)

    elif dataset_type == 'db':
        try:
            dataset = Dataset.objects.get(dataset_name=dataset)
            data_table = apps.get_model(DATA_TABLES_APP, dataset.dataset_django_model)
            data = data_table.objects.all()
            variables = Variable.objects.filter(dataset_relation=dataset.id).order_by('id')
        except Exception as e:
            log.error('Dataset or corresponding variables not found in order to complete the 2d histogram.')
            log.error(e)
            return e, 400

        # The order of the variables is decided to be like this: column, row, value.
        try:
            col_ordering = heatmap_ordering(col_order, variables, 0)
            row_ordering = heatmap_ordering(row_order, variables, 1)
            data = heatmap_ordering_method(col_ordering, data, row_ordering)
        except Exception as e:
            log.error('Error while ordering the columns or rows for the histogram 2d')
            log.error(e)
            return e, 400

        final_data = reformat_chart_data(data, variables)
        # If guides/ranges are used, the dataset of the guides has to be declared explicitly in the request
        row_ranges_data = heatmap_categorisation(row_categorisation_dataset, workspace=[workspace])
        col_ranges_data = heatmap_categorisation(col_categorisation_dataset, workspace=[workspace])
    elif dataset_type == 'query':
        final_data = heatmap_query(dataset)
        row_ranges_data = heatmap_categorisation(row_categorisation_dataset)
    elif dataset_type == 'dataframe':
        pass

    return final_data, row_ranges_data, col_ranges_data


def heatmap_categorisation(categorisation_dataset, workspace=['pr_global', 'pr_eu']):
    '''
    This method is responsible for categorising the data in the columns and rows of the heatmap
    :param categorisation_dataset: the name of a table in the database that categorises the rows, and columns in a specific way
    :return: A json file in the suitable format for categorising data of the rows or the columns into groups
    '''
    ranges_data = []
    if categorisation_dataset != '':
        ranges_table = apps.get_model(DATA_TABLES_APP, categorisation_dataset).objects.filter(workspace__in=workspace)
        for el in ranges_table:
            dict_el = {'guide_from': el.guide_from, 'guide_to': el.guide_to, 'value': el.value}
            ranges_data.append(dict_el)
    return ranges_data


def heatmap_ordering_method(col_ordering, data, row_ordering):
    '''
    This method is used for multi-level ordering the data of the rows or the columns (or both) in the heatmap
    :param col_ordering: the field according to which the columns are going to be ordered
    :param data: The raw data retrieved from the database
    :param row_ordering: the field according to which the rows are going to be ordered
    :return: Ordered data according to given fields
    '''
    if (col_ordering is None) and (row_ordering is None):
        pass
    elif col_ordering is None:
        data = data.order_by(row_ordering)
    elif row_ordering is None:
        data = data.order_by(col_ordering)
    else:
        data = data.order_by(col_ordering, row_ordering)
    return data


def heatmap_ordering(order, variables, var_position):
    '''
    This method orders the data according to a given field
    :param order: the name of the filed according to which the ordering takes place
    :param variables: The selected variables that are used in the heatmap
    :param var_position: The position of the variable in the table
    :return: Ordered data
    '''
    ordering = None
    django_model = apps.get_model(DATA_TABLES_APP, variables[var_position].variable_table_name)
    fields = django_model._meta.get_fields()
    for field in fields:
        if order == field.name:
            ordering = str(variables[var_position].var_name) + "__" + str(field.name)
    return ordering


# ADDITIONAL METHODS
def reformat_chart_data(data, variables):
    """
    This method is used for reformatting the ORM data to the suitable format for the visualiser
    :param data: The data records retrieved from the database
    :param variables: The specific variables whose columns are going to be used in the chart
    :return: Data in a suitable format for the heatmap chart
    """

    final_data = []
    for el in data:
        dictionary = {}
        for var in variables:
            if var.variable_table_name is None:
                dictionary[var.var_name] = getattr(el, var.var_name)
            else:
                var_table = apps.get_model(DATA_TABLES_APP, var.variable_table_name)
                var_table_obj = var_table.objects.get(id=getattr(el, var.var_name).id)
                value = var_table_obj.title
                dictionary[var.var_name] = value
        final_data.append(dictionary)
    return final_data
