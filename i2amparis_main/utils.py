from django.apps import apps
from django.db.models import F

from i2amparis_main.models import *


def get_model_by_db_table(db_table):
    for model in apps.get_models():
        if model._meta.db_table == db_table:
            return model
    else:
        # here you can do fallback logic if no model with db_table found
        raise ValueError('No model found with db_table {}!'.format(db_table))
        # or return None


def get_initial_detailed_conf_analysis_form_data(interface):
    if interface == 'pr_global':
        all_models = [el['name'] for el in DataVariablesModels.objects.filter(
            name__in=['42', 'e3me', 'gcam', 'gemini_e3', 'ices', 'muse', 'tiam']).values('name')]
        all_scenarios = [el['name'] for el in ScenariosRes.objects.exclude(name='EUWWH').values('name')]
        all_regions = [el['name'] for el in RegionsRes.objects.values('name')]
        all_variables = [el['variable_name'] for el in PRWMetaData.objects.distinct().values('variable_name')]
        metadata = PRWMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    elif interface == 'pr_eu':
        all_models = [el['name'] for el in DataVariablesModels.objects.filter(
            name__in=['aladin', 'eu_times', 'e3me', 'forecast', 'gcam', 'gemini_e3', 'ices', 'muse', 'nemesis', 'tiam', '42']).values('name')]
        all_scenarios = [el['name'] for el in ScenariosRes.objects.filter(name='EUWWH').values('name')]
        all_regions = [el['name'] for el in RegionsRes.objects.filter(name='EU').values('name')]
        all_variables = [el['variable_name'] for el in PRWEUMetaData.objects.distinct().values('variable_name')]
        metadata = PRWEUMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    elif interface == 'pr_covid':
        all_models = ['gcam', 'gemini_e3', 'tiam']
        all_scenarios = [el['name'] for el in ScenariosRes.objects.filter(name__contains='COVID').values('name')]
        all_regions = ['EU','China','USA','India','Japan','Canada']
        all_variables = ["PV Investment Share","CSP Investment Share","Onshore wind Investment Share",
            "Offshore wind Investment Share","Geothermal Investment Share","Nuclear Investment Share","Biomass Investment Share",
            "Hydro Investment Share","Biofuels Investment Share"]
        metadata = COVIDMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    elif interface == 'pr_feasibility':
        all_models = [el['model_name'] for el in FeasibilityMetaData.objects.distinct().values('model_name')]
        all_scenarios = [el['scenario_name'] for el in FeasibilityMetaData.objects.distinct().values('scenario_name')]
        all_regions = [el['region_name'] for el in FeasibilityMetaData.objects.distinct().values('region_name')]
        all_variables = [el['variable_name'] for el in FeasibilityMetaData.objects.distinct().values('variable_name')]
        metadata = FeasibilityMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    elif interface == 'pr_ndca':
        all_models = [el['model_name'] for el in NDCAMetaData.objects.distinct().values('model_name')]
        all_scenarios = [el['scenario_name'] for el in NDCAMetaData.objects.distinct().values('scenario_name')]
        all_regions = [el['region_name'] for el in NDCAMetaData.objects.distinct().values('region_name')]
        all_variables = [el['variable_name'] for el in NDCAMetaData.objects.distinct().values('variable_name')]
        metadata = NDCAMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    elif interface == 'pr_fitfor55':
        all_models = [el['model_name'] for el in EUPathwayMetaData.objects.distinct().values('model_name')]
        all_scenarios = [el['scenario_name'] for el in EUPathwayMetaData.objects.distinct().values('scenario_name')]
        all_regions = [el['region_name'] for el in EUPathwayMetaData.objects.distinct().values('region_name')]
        all_variables = [el['variable_name'] for el in EUPathwayMetaData.objects.distinct().values('variable_name')]
        metadata = EUPathwayMetaData
        return all_models, all_scenarios, all_regions, all_variables, metadata
    else:
        print('No interface provided or no interface exists with that name!')



def create_info_for_var_harmonisation_heatmaps(harm_data_sources_links, var_mod_data):
    var_mod = list(var_mod_data.values('var_unit', 'var_timespan', mod=F('model__name'), var=F('variable__var_name')))
    for el in var_mod:
        temp_sources = harm_data_sources_links.filter(model__name=el['mod'],
                                                      variable__var_name=el['var']).values(
            "var_source_info", "var_source_url", "title__title")
        source_list = []
        temp_title = ''
        info_dict = {}
        for source in temp_sources:
            if source['title__title'] == temp_title or temp_title == '':
                temp_title = source['title__title']
                source_list.append(
                    {'var_source_url': source['var_source_url'], 'var_source_info': source['var_source_info']})
            else:
                info_dict[temp_title] = source_list
                source_list = []
                temp_title = source['title__title']
                source_list.append(
                    {'var_source_url': source['var_source_url'], 'var_source_info': source['var_source_info']})
        if temp_title != "":
            info_dict[temp_title] = source_list
        el['source_info'] = info_dict
    return var_mod