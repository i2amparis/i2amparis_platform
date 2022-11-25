from django.core.management.base import BaseCommand, CommandError
from i2amparis_main.models import ResultsComp, PRWMetaData, PRWEUMetaData, ModelsInfo, Harmonisation_Variables, \
    HarmDataNew, HarmDataSourcesLinks
from django.apps import apps
from django.db.models import F
import json


class Command(BaseCommand):
    help = 'Create cache files for harmonisation heatmaps'

    def handle(self, *args, **options):

        var_mod_data = HarmDataNew.objects.all()
        harm_data_sources_links = HarmDataSourcesLinks.objects.all()
        var_mod = list(
            var_mod_data.values('var_unit', 'var_timespan', mod=F('model__name'), var=F('variable__var_name')))
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
        try:
            cached_file = open("cached_data/harmonisation_heatmaps/pr_harmonisation_heatmap.json", "w")
            json.dump(var_mod, cached_file)
            cached_file.close()
            self.stdout.write('Successfully cached data for PR Global Variable Harmonisation Heatmap.')
        except:
            self.stdout.write('Caching data for PR Global Variable Harmonisation Heatmap failed. Command Terminated.')

