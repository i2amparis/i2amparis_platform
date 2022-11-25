import json

from i2amparis_main.models import ModelsInfo, ScenariosRes, RegionsRes, HistoricalData
from data_manager.models import Query
from data_manager.utils import query_execute
import pandas as pd

from data_manager.utils import clean_dictionary_list_from_zero_values, clean_dictionary_list_from_null_values

'''This file contains a set of functions used for the reshaping of data in order to be suitable for the visualiser.
At first the query is executed using the query_execute() function and are reprocessed using pandas Dataframes to be 
converted into a suitable format for each visualisation.'''


def line_chart_query(query_id):
    '''
       This method defines which query is going to be executed for the creation of a line chart
       :param query_id: The query_id of the query to be executed in order to retrieve data for the line chart
       :return: The results of the executed query
    '''
    query_name = Query.objects.get(id=query_id).query_name
    results = []
    if query_name == 'scientific_tool_query':
        results = scentific_tool_query(query_id)
    elif query_name in ['wwhglobal_pub_total_co2_emissions_cp_query', 'wwhglobal_pub_total_co2_emissions_ndc_query']:
        results = max_min_query(query_id, ["year", "model__name"], 'model', 'scenario', 'year')
    elif query_name in ['wwheu_pub_total_co2_emissions_query', 'fossil_energy_co2_query',
                        'global_approximate_temperature_query', 'global_ccs_1_query', 'global_ccs_2_query',
                        'global_primary_energy_query', 'eu_wwh_scientific_co2_emissions_query',
                        'eu_wwh_scientific_imported_fuels_coal_query', 'eu_wwh_scientific_imported_fuels_gas_query',
                        'eu_wwh_scientific_imported_fuels_oil_query',
                        'eu_wwh_scientific_investments_energy_supply_query', 'wwhglobal_pub_global_temp_query',
                        'eu_wwh_scientific_investments_power_generation_query',
                        'wwhglobal_pub_ccs1_query', 'wwhglobal_pub_ccs2_query', 'wwhglobal_pub_final_energy_sector_industry_query',
                        'wwhglobal_pub_final_energy_sector_transportation_query', 'wwhglobal_pub_final_energy_sector_buildings_query',
                        'energy_co2_query','industry_co2_query','feasibility_temperature_query','ida_pub_ida_benchmarking_query']:
        results = combined_linechart_data_projection(query_id, 'model', 'scenario', 'year')
    elif query_name in ['wwheu_pub_imported_fuels_query']:
        results = simple_linechart_data_projection(query_id, 'model', 'year')
    elif query_name in ['wwhglobal_pub_global_temp_historical_query', 'wwhglobal_pub_total_co2_emissions_cp_historical_query',
                        'wwhglobal_pub_total_co2_emissions_ndc_historical_query']:
        results = simple_linechart_data_projection(query_id, 'variable', 'year')
    elif query_name in ['wwheu_pub_co2_ccs_ag_co2_reduction_query', 'eu_wwh_scientific_ccs2_query']:
        results = variable_to_variable_linechart_data(query_id, 'Extra_CO2_reduction_ratio', True,
                                                      'Extra_CO2_Captured_with_CCS', False, 'model', 'variable')
    elif query_name in ['wwheu_pub_import_dependency_query', 'eu_wwh_scientific_import_ratio_query']:
        results = variable_to_variable_linechart_data(query_id, 'Extra_CO2_reduction_ratio', True,
                                                      'Extra_Import_Dependency', True, 'model', 'variable')
    elif query_name in ['wwheu_pub_electrification_ir_co2_reduction_query',
                        'eu_wwh_scientific_electrification_ratio_query']:
        results = variable_to_variable_linechart_data(query_id, 'Extra_CO2_reduction_ratio', True,
                                                      'Extra_Electricity_Share', True, 'model', 'variable')
    return results


def column_chart_query(query_id):
    '''
       This method defines which query is going to be executed for the creation of a column chart
       :param query_id: The query_id of the query to be executed in order to retrieve data for the column chart
       :return: The results of the executed query
    '''
    query_name = Query.objects.get(id=int(query_id)).query_name
    results = []
    if query_name == 'scientific_tool_query':
        results = scentific_tool_query(query_id)
    elif query_name in ['primary_energy_by_fuel_avg_models_query', 'final_energy_by_fuel_avg_models_query']:
        results = variable_clustered_groups_per_parameter(query_id, 'model_id', 'year')
    elif query_name in['primary_energy_by_fuel_avg_scenarios_query', 'final_energy_by_fuel_avg_scenarios_query']:
        results = variable_clustered_groups_per_parameter(query_id, 'scenario_id', 'year')
    elif query_name in ['wwheu_pub_energy_co2_emissions_by_sector_query', 'wwheu_pub_electrification_fec_query',
                        'wwheu_pub_hydrogen_production_by_fuel_query', 'wwheu_pub_hydrogen_electricity_comp_ind_query',
                        'wwheu_pub_hydrogen_electricity_comp_trans_query',
                        'eu_wwh_scientific_electrification_sector_query',
                        'eu_wwh_scientific_hydrogen_by_fuel_query', 'eu_wwh_scientific_hydrogen_industry_query',
                        'eu_wwh_scientific_hydrogen_transport_query', 'eu_wwh_scientific_primary_by_fuel_query',
                        'eu_wwh_scientific_final_by_sector_query', 'eu_wwh_scientific_co2_emisssions_by_sector_query',
                        'eu_wwh_scientific_investments_by_gen_tech_query']:
        results = variable_clustered_groups_per_parameter(query_id, 'model_id', 'year')
    elif query_name in ['wwhglobal_pub_final_energy_ft_2020_query', 'wwhglobal_pub_final_energy_ft_2030_query',
                        'wwhglobal_pub_final_energy_ft_2050_query', 'wwhglobal_pub_final_energy_sector_2020_query',
                        'wwhglobal_pub_final_energy_sector_2030_query', 'wwhglobal_pub_final_energy_sector_2050_query',
                        'covid_pub_covid_portfolio_query','covid_pub_covid_impacts_co2_query',
                        'covid_pub_covid_impacts_jobs_2025_query','covid_pub_covid_impacts_jobs_2030_query',
                        'ida_pub_ida_levers_query']:
        results = variable_clustered_groups_per_parameter(query_id, 'scenario_id', 'model__title')
    elif query_name in ['wwheu_pub_co2_ccs_by_sector_query', 'eu_wwh_scientific_ccs1_query']:
        results = wwheu_pub_co2_ccs_by_sector(query_id)

    elif query_name in ['wwhglobal_pub_total_co2_emissions_cp_ranges_query']:
        results = dumbell_max_min(query_id, ["model__name", "year"], 'model', 'scenario',
                                  ['PR_CurPol_EI', 'PR_CurPol_CP'],
                                  'PR_Baseline', [2050, 2045], 'max')
    elif query_name in ['wwhglobal_pub_total_co2_emissions_ndc_ranges_query']:
        results = dumbell_max_min(query_id, ["model__name", "year"], 'model', 'scenario', ['PR_NDC_EI', 'PR_NDC_CP'],
                                  'PR_Baseline', [2050, 2045], 'max')
    elif query_name in ['wwhglobal_pub_global_temp_ranges_query']:
        results = dumbell_max_min(query_id, ["model__name", "year"], 'model', 'scenario',
                                  ['PR_CurPol_CP', 'PR_CurPol_EI', 'PR_NDC_CP', 'PR_NDC_EI'], None, [], '')

    elif query_name == 'rrf_classification_1_query':
        results = rrf_classification_query(query_id, 'first_classification')
    elif query_name == 'rrf_classification_2_query':
        results = rrf_classification_query(query_id, 'second_classification')
    return results


def pie_chart_query(query_id):
    '''
       This method defines which query is going to be executed for the creation of a pie chart
       :param query_id: The query_id of the query to be executed in order to retrieve data for the pie chart
       :return: The results of the executed query
    '''
    query_name = Query.objects.get(id=int(query_id)).query_name
    results = []
    if query_name == 'scientific_tool_query':
        results = scentific_tool_query_agg(query_id)
    return results


def rrf_classification_query(query_id, classification):
    '''
        This method is the execution of the classification query for the rrf policy workspace
        :param query_id: The query_id of the query to be executed in order to retrieve data
        :param classification: The classification that is going to be used for the reshaping of data
    '''
    app_params = json.loads(Query.objects.get(id=int(query_id)).parameters)
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []

    budget_data = df.pivot(index="country", columns=classification, values="budget").reset_index().fillna(0)
    total_data = df.groupby(by="country")['budget'].sum().reset_index().rename(columns={"budget": "total"})
    total_data['none'] = 0
    final_data = list(pd.merge(budget_data, total_data, how="inner", on="country").fillna(0).to_dict(
        'index').values())
    return final_data


def scentific_tool_query_agg(query_id):
    '''
    This method is the execution of the query for creating data for the advanced scientific tool piechart
    :param query_id: The query_id of the query to be executed in order to retrieve data for the advanced scientific tool piechart
    '''
    app_params = json.loads(Query.objects.get(id=int(query_id)).parameters)
    multiple_field = app_params['additional_app_parameters']['multiple_field']
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    final_data = list(
        df.pivot(index="year", columns=multiple_field + "__name", values="value").reset_index().fillna(-999999).to_dict(
            'index').values())
    clean_final_data = clean_dictionary_list_from_null_values(final_data)
    clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

    return clean_final_data


def primary_energy_by_fuel_avg_query(query_id, grouping_val):
    '''
     This method is the execution of the query for creating data for the intro page of the advanced scientific tool for column charts that show global primary energy per model averaged across scenarios
     :param grouping_val: This variable shows whether the grouping is done across models or scenarios
     :param query_id: The query_id of the query to be executed in order to retrieve data for the advanced scientific tool columnchart
     '''
    if grouping_val == 'model_id':
        record_title = 'model_title'
        grouping_var_data = ModelsInfo.objects.all().values()
    else:
        record_title = 'title'
        grouping_var_data = ScenariosRes.objects.all().values()
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    else:
        grouping_var_df = pd.DataFrame.from_records(grouping_var_data)[['id', record_title]].rename(
            columns={'id': grouping_val, record_title: 'title'})

        joined_df = pd.merge(left=df, right=grouping_var_df, left_on=grouping_val, right_on=grouping_val)

        joined_df.drop(grouping_val, axis=1, inplace=True)
        joined_df = joined_df.rename(columns={'title': grouping_val})

        joined_df[grouping_val + '_var'] = joined_df[grouping_val] + '_' + joined_df['variable__name']
        final_df = joined_df.pivot(index="year", columns=grouping_val + "_var", values="value").reset_index().fillna(
            -999999)
        final_data = list(final_df.to_dict('index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def max_min_query(query_id, group_by_list, timeseries, instances, pivot_var):
    '''
        This method is the execution of the query for creating data for charts that compare two instances of several time
        series, including a colored area between the two instances of each time series, showing the range.
        :param query_id: The query_id of the query to be executed in order to retrieve data
        :param group_by_list: This is a list of the parameters according to which the grouping of the data takes places.
        :param timeseries: The timeseries to be compared (ie. model, scenario, etc.)
        :param instances: The different instances of timeseries (ie. model, scenario etc.)
        :param pivot_var: The parameter according to which the dataframe will pivot. This defines the final rows.
        It is used  for extracting the minimum and maximum values of the colored range.
    '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)

    if df.empty:
        return []
    else:
        # Creating the min-max ranges
        max_df = df.groupby(by=group_by_list).max().reset_index()
        max_df[instances + '_' + timeseries] = max_df[timeseries + '__name'] + ' Maximum'
        max_df = max_df.drop(['variable__name', 'region__name'], axis=1)
        min_df = df.groupby(by=group_by_list).min().reset_index()
        min_df[instances + '_' + timeseries] = min_df[timeseries + '__name'] + ' Minimum'
        min_df = min_df.drop(['variable__name', 'region__name'], axis=1)

        df[instances + '_' + timeseries] = df[timeseries + '__name'] + '_' + df[instances + '__name']
        df = df.drop(['scenario__name', 'variable__name', 'model__name', 'region__name'], axis=1)
        final_df = pd.concat([min_df, max_df, df]).reset_index()
        final_data = list(
            final_df.pivot(index=pivot_var, columns=instances + "_" + timeseries, values="value").reset_index().fillna(
                -999999).to_dict(
                'index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def dumbell_max_min(query_id, group_by_list, timeseries, max_min_parameter, range_list, points,
                    point_pos, select_min_max):
    '''
        This method is the execution of the query for getting the data for the dumbell charts showing ranges in the workspace
        :param query_id: The query_id of the query to be executed in order to retrieve data for the chart
        :param group_by_list: it is the parameter according to which the grouping takes place
        :param range_list: this list contains the names of the parameter used for the ranges in the chart
        :param points: the name of the parameter used for the points on the chart
        :param point_pos: The actual position of the visualised point i.e. a specific year (it is a list because some
        parameters may have different positions due to missing values
        :param select_min_max: can be max or min. Selects min or max valued element of the point_pos list.
        '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    bars_df = df[df[max_min_parameter + '__name'].isin(range_list)]
    if points is not None:
        # This is incredibly complex because of the inconsistency in the data.
        markers_df = df[df[max_min_parameter + '__name'] == points]
        markers_df = markers_df.loc[markers_df['year'].isin(point_pos)]
        if select_min_max == 'max':
            markers_df = markers_df.loc[markers_df.groupby(by=timeseries+'__name')['year'].idxmax()]
        else:
            markers_df = markers_df.loc[markers_df.groupby(by=timeseries + '__name')['year'].idxmin()]
        markers_df[timeseries + '_' + max_min_parameter] = markers_df[timeseries + '__name'] + '_baseline'
        markers_df = markers_df.drop(['year', 'model__name', 'scenario__name', 'region__name', 'variable__name'], axis=1)

    if df.empty:
        return []
    else:
        # Creating the min-max ranges
        max_df = bars_df.groupby(by=group_by_list).max().reset_index()
        max_df = max_df.drop(['variable__name', 'region__name', 'scenario__name'], axis=1)
        max_df = max_df.rename(columns={'value': 'open'})
        min_df = bars_df.groupby(by=group_by_list).min().reset_index()
        min_df = min_df.drop(['variable__name', 'region__name', 'scenario__name'], axis=1)
        min_df = min_df.rename(columns={'value': 'close'})
        min_max_df = pd.merge(left=max_df, right=min_df, left_on=[timeseries + '__name', 'year'],
                              right_on=[timeseries + '__name', 'year'])
        min_max_df['range'] = min_max_df['open'] - min_max_df['close']
        min_max_df = min_max_df.drop(['year'], axis=1)
        min_max_df = min_max_df.loc[min_max_df.groupby(by=timeseries + '__name')['range'].idxmax()]
        min_max_df = min_max_df.drop(['range'], axis=1)
        new_max_df = min_max_df
        new_max_df[timeseries + '_' + max_min_parameter] = new_max_df[timeseries + '__name'] + '_open'
        new_max_df = new_max_df.drop(['close', timeseries + '__name'], axis=1).rename(columns={'open': 'value'})
        new_min_df = min_max_df
        new_min_df[timeseries + '_' + max_min_parameter] = new_min_df[timeseries + '__name'] + '_close'
        new_min_df = new_min_df.drop(['open', timeseries + '__name'], axis=1).rename(columns={'close': 'value'})
        if points is not None:
            new_min_max_df = pd.concat([new_max_df, new_min_df, markers_df])
        else:
            new_min_max_df = pd.concat([new_max_df, new_min_df])
        final_data = list(
            new_min_max_df.set_index(timeseries + '_' + max_min_parameter).to_dict().values())
        final_data[0]['category'] = ''

        return final_data


def combined_linechart_data_projection(query_id, timeseries, instances, pivot_var):
    '''
        This method is the execution of the query for creating data for a simple data projection
        :param query_id: The query_id of the query to be executed in order to retrieve data for the linechart
        :param timeseries: The timeseries to be projected (ie. model, scenario, etc.)
        :param instances: The different instances of timeseries (ie. model, scenario etc.)
        :param pivot_var: The parameter according to which the dataframe will pivot. This defines the final rows.
        '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)

    if df.empty:
        return []
    else:
        df[instances + '_' + timeseries] = df[timeseries + '__name'] + '_' + df[instances + '__name']
        df = df.drop(['scenario__name', 'variable__name', 'model__name', 'region__name'], axis=1)
        final_data = list(
            df.pivot(index=pivot_var, columns=instances + "_" + timeseries, values="value").reset_index().fillna(
                -999999).to_dict(
                'index').values())

        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def simple_linechart_data_projection(query_id, timeseries, pivot_var):
    '''
        This method is the execution of the query for creating data for simple data projection
        :param query_id: The query_id of the query to be executed in order to retrieve data for the linechart
        :param timeseries: The timeseries to be projected (ie. model, scenario, etc.)
        :param pivot_var: The parameter according to which the dataframe will pivot. This defines the final rows.

        '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)

    if df.empty:
        return []
    else:
        final_data = list(
            df.pivot(index=pivot_var, columns=timeseries + '__name', values="value").reset_index().fillna(
                -999999).to_dict(
                'index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def variable_to_variable_linechart_data(query_id, x_axis, x_axis_ratio, y_axis, y_axis_ratio, multiple_val,
                                        axis_values):
    '''
        This method is the execution of the query for creating data for a chart that uses two instances of the same
        parameter to showcase their relation. For this chart, only one parameter can have multiple values that are
        presented as different timeseries.
        :param query_id: The query_id of the query to be executed in order to retrieve data
        :param x_axis: The value of the parameter used for the x_Axis
        :param x_axis_ratio: True if the parameter is a percentage %
        :param y_axis: The value of the parameter used for the y_Axis
        :param y_axis_ratio: True if the parameter is a percentage %
        :param multiple_val: The only parameter that can have multiple values
        :param axis_values: The parameter type that is going to be used for the two axes
        '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    else:
        df = df.pivot(index=["year", multiple_val + "__name"], columns=axis_values + "__name",
                      values="value").reset_index()
        if x_axis_ratio:
            df[x_axis] = 100 * df[x_axis]
        if y_axis_ratio:
            df[y_axis] = 100 * df[y_axis]
        df = df.pivot(index=x_axis, columns=multiple_val + "__name", values=y_axis)
        final_data = list(
            df.reset_index().fillna(-999999).to_dict(
                'index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def variable_clustered_groups_per_parameter(query_id, grouping_val, pivot_var):
    '''
     This method is the execution of the query for creating data for the co2 emissions by sector for the EU public interface
     :param grouping_val: This variable shows whether the grouping is done across models or scenarios
     :param query_id: The query_id of the query to be executed in order to retrieve data for the advanced scientific tool columnchart
     :param pivot_var: The parameter according to which the final rows of the data will be created (the dataframe will pivot)'''

    if grouping_val == 'model_id':
        record_title = 'model_title'
        grouping_var_data = ModelsInfo.objects.all().values()
    else:
        record_title = 'title'
        if grouping_val == 'scenario_id':
            grouping_var_data = ScenariosRes.objects.all().values()
        elif grouping_val == 'region_id':
            grouping_var_data = RegionsRes.objects.all().values()
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    else:
        grouping_var_df = pd.DataFrame.from_records(grouping_var_data)[['id', record_title]].rename(
            columns={'id': grouping_val, record_title: 'title'})

        joined_df = pd.merge(left=df, right=grouping_var_df, left_on=grouping_val, right_on=grouping_val)

        joined_df.drop(grouping_val, axis=1, inplace=True)
        joined_df = joined_df.rename(columns={'title': grouping_val})

        joined_df[grouping_val + '_var'] = joined_df[grouping_val] + '_' + joined_df['variable__name']
        final_df = joined_df.pivot(index=pivot_var, columns=grouping_val + "_var", values="value").reset_index().fillna(
            -999999)
        final_data = list(final_df.to_dict('index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

        return clean_final_data


def wwheu_pub_co2_ccs_by_sector(query_id):
    '''
     This method is the execution of the query for creating data for the co2 emissions by sevtor for the EU public interface
     :param grouping_val: This variable shows whether the grouping is done across models or scenarios
     :param query_id: The query_id of the query to be executed in order to retrieve data for the advanced scientific tool columnchart
     '''
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    else:
        # Creating the min-max ranges
        df = df.drop(['region__name'], axis=1)
        df = df.pivot(index=["year"], columns="variable__name", values="value")
        final_data = list(
            df.reset_index().fillna(-999999).to_dict(
                'index').values())
        clean_final_data = clean_dictionary_list_from_null_values(final_data)
        clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)
        return clean_final_data


def heatmap_query(query_id):
    '''
    This method defines which query is going to be executed for the creation of a heatmap chart
    :param query_id: The query_id of the query to be executed in order to retrieve data for the heatmap chart
    :return: The results of the executed query
    '''
    query_name = Query.objects.get(id=query_id).query_name
    if query_name == 'var_harmonisation_on_demand':
        results = var_harmonisation_on_demand(query_id)
        return results


def scentific_tool_query(query_id):
    '''
    This method is the execution of the query for creating data for the advanced scientific tool used in different
    workspaces.
    :param query_id: The query_id of the query to be executed in order to retrieve data for the advanced scientific tool
    '''
    app_params = json.loads(Query.objects.get(id=int(query_id)).parameters)
    multiple_field = app_params['additional_app_parameters']['multiple_field']
    data, add_params = query_execute(query_id)
    df = pd.DataFrame.from_records(data)
    if df.empty:
        return []
    final_data = list(
        df.pivot(index="year", columns=multiple_field + "__name", values="value").reset_index().fillna(-999999).to_dict(
            'index').values())
    clean_final_data = clean_dictionary_list_from_null_values(final_data)
    clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)

    return clean_final_data


def var_harmonisation_on_demand(query_id):
    '''
    This method is the execution of the query for creating data for the on-demand variable harmonisation heatmap
    :param query_id: The query_id of the query to be executed in order to retrieve data for the on-demand variable harmonisation heatmap
    :return:
    '''

    from i2amparis_main.models import DatasetOnDemandVariableHarmonisation
    json_params = get_query_parameters(query_id)
    model_list = []
    if 'model_list' in json_params.keys():
        model_list = json_params['model_list']
    results = DatasetOnDemandVariableHarmonisation.objects.filter(model__name__in=model_list).order_by(
        "variable__order")
    var_mod = []
    for el in results:
        dict_el = {
            "model": el.model.title,
            "var": el.variable.var_title,
            "status": el.io_status,
        }
        var_mod.append(dict_el)

    return var_mod


def get_query_parameters(query_id):
    '''
    This method is used for retrieving all the necessary parameters of the query
    :param query_id: The query_id whose parameters are extracted
    :return: A JSON object containing all query parameters
    '''
    query = Query.objects.get(id=query_id)
    parameters = query.parameters
    q_params = json.loads(parameters)
    return q_params

# This was used for the quantity comparison scientific tool that was dismissed

# def quantity_comparison_query(query_id):
#     data, add_params = query_execute(query_id)
#     df = pd.DataFrame.from_records(data)
#     grouping_val = add_params['grouping_var']
#     var_table_name = Variable.objects.get(var_name=grouping_val).variable_table_name
#     if df.empty:
#         return []
#     if var_table_name is None:
#         final_data = list(
#             df.pivot(index=grouping_val, columns="scenario__name", values="value").reset_index().fillna(
#                 -999999).to_dict(
#                 'index').values())
#     else:
#         grouping_var_table = apps.get_model(DATA_TABLES_APP, var_table_name)
#         grouping_var_data = grouping_var_table.objects.all().values()
#         grouping_var_df = pd.DataFrame.from_records(grouping_var_data)[['id', 'title', 'reg_type']].rename(
#             columns={'id': grouping_val})
#
#         joined_df = pd.merge(left=df, right=grouping_var_df, left_on=grouping_val, right_on=grouping_val)
#         joined_df.drop(grouping_val, axis=1, inplace=True)
#         joined_df = joined_df.rename(columns={'title': grouping_val})
#         pivoted_df = joined_df.pivot(index=[grouping_val, 'reg_type'], columns=["scenario__name"],
#                                      values="value").sort_values('reg_type').reset_index()
#         pivoted_df.drop('reg_type', axis=1, inplace=True)
#         final_data = list(pivoted_df.fillna(-999999).to_dict('index').values())
#     clean_final_data = clean_dictionary_list_from_null_values(final_data)
#     clean_final_data = clean_dictionary_list_from_zero_values(clean_final_data)
#
#     return clean_final_data
