from i2amparis_main.models import *
import random
from random import shuffle

from .retrievegranularities import  RetrieveGranularities



class RetriveDB:
    def __init__(self, model_name):
        self.model_name = model_name
        models_lst = list(ModelsInfo.objects.values_list('model_name', flat=True))
        if self.model_name in models_lst:
            self.model_id = ModelsInfo.objects.get(model_name=self.model_name).id
        else:
            self.model_id = ModelsInfo.objects.all().order_by('ordering')[0].id
        self.retrieve_granularity = RetrieveGranularities(self.model_id).data

    def create_json(self):
        """
      Get the model_name and retrive countries from database
      and create the json which need the map to represent the
      countries
      We must have two case one where model haven't region and second where there are regions
      1) In first case each country is a 'group of countries', also the 'name' of the group will be the name of country
      2) In second case each region is a group of countries

      :param model_name:
      :return:
      """
        counter = 0
        data = []
        # First we take the list of region for the given model id
        regions = list(Regions.objects.filter(model_name=self.model_id).values_list('region_name', flat=True))
        color_list = self.generate_colors(len(regions))
        # Then loop in regions and get the countries, name and code of each one
        print (regions)
        for k,region in enumerate(regions):
            temp = Regions.objects.get(region_name=region)
            # Get the id of the region
            region_id = temp.id
            # Get the description of region
            region_descr = temp.descr
            countries_of_region = list(Countries.objects.filter(region_name=region_id).values_list(
                'country_name', 'country_code'))
            # Make a list which each element is a dict with keys tittle:<name of country>,id:<country code>,
            # descr:<descr of region>
            countries_list = list(map(lambda x: {'title': x[0], 'id': x[-1], 'descr': region_descr},
                                      countries_of_region))
            if len(countries_list) == 1:
                selected_color = color_list[0]
                # print('!!region has one country!!')
            else:
                counter = counter + 1
                selected_color = color_list[counter]
            temp_dict = {
                "name": temp.region_title,
                "color": selected_color,
                "data": countries_list
            }
            data.append(temp_dict)
        return data

    def create_models_btn(self, harmonisation=0):
        """
        Retrive all models names and create the buttons

        :return:
        """
        # Get all table of models
        if harmonisation == 1:
            models_data = ModelsInfo.objects.filter(harmonisation=1).order_by('ordering')
        else:
            models_data = ModelsInfo.objects.all().order_by('model_title')
        # Get the titles of each model
        model_dict = {}
        for el in models_data:
            new_dict = {}
            new_dict['description'] = el.short_description
            new_dict['icon'] = el.icon
            new_dict['title'] = el.model_title
            new_dict['long_title'] = el.long_title
            model_dict[el.model_name] = new_dict
        return model_dict

    def generate_colors(self, n):
        color_list = ['#8a941f',  '#e68200', '#066c7a',
                      '#c7c78a', '#91bec4', '#ffb049', '#0aaec5',
                      '#454a0f', '#ab6100', '#033a42', '#758000', '#434747', '#26909e', '#a89172', '#8fbec4', '#a89fc9',
                      '#5a5275', '#e68200', '#066c7a'
                      ]
        color_list = color_list
        return color_list

    def create_model_json(self):
        """
        Create the self.model_json,
        The model_json is a dict with keys the names of models and value  a dict with two keys
        descr, which include the description of model  and
        heading, which for now is remain empty

        :return:
        """
        data = list(ModelsInfo.objects.all().values_list('model_name', 'model_descr'))
        data = list(map(lambda x: {x[0], {'descr': x[1], 'heading': ''}}, data))
        return dict(j for i in data for j in i.items())
