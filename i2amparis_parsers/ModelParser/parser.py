import xlrd

from i2amparis_main.models import *

class Parser:
    def __init__(self, excel_name):
        self.excel_loc = (excel_name)
        self.data_dict = {}
        self.wb = xlrd.open_workbook(self.excel_loc)
        self.sheets_name = [
                                'Sectors',
                                'MitigationAdaptation',
                                'SocioEcon',
                                'Emissions',
                                'Policies',
                                'SDGs',
                                'Model_Info',
                                'Regions',
                                'Comments'
                                ]
    def _return_sheet(self, sheet_name):
        """

        :param sheet_name:
        :return: object sheet of given name
        """
        return self.wb.sheet_by_name(sheet_name)

    def _retrieve_data(self, row_range, col_range, sheet_name, sheet_obj):
        """

        :param row_range:
        :param col_range:
        :param sheet_name:
        :param sheet_obj:
        :return:a dict with key the sheet_name and value a list of lists which each list contains the row of data
        """
        data = []
        for row in row_range:
            temp = []
            for col in col_range:
                temp.append(
                    sheet_obj.cell_value(row, col)
                )
            data.append(temp)
        return {
                    sheet_name: data
                }

    def _sectors(self):
        """
        Read the sheet Sectors

        :return: a dict with key Sectors and value a list of lists which each list contains the row of data
        """
        sheet_name = self.sheets_name[0]
        # The actual data have range for row=[1,60] and col=[0,3]
        self.sector_dict = self._retrieve_data(range(1, 61), range(0, 4), sheet_name, self._return_sheet(sheet_name))

    def _mitigationadaptation(self):
        """
        Read the tab MitigationAdaptation
        :return: a dict with key MitigationAdaptation and value a list of lists which each list contains the row of data
        """
        sheet_name = self.sheets_name[1]
        # The actual data have range for row=[1,105] and col=[0,3]
        self.mitigationadaptation_dict = self._retrieve_data(range(1, 106), range(0, 4),
                                                             sheet_name, self._return_sheet(sheet_name))

    def _socioecons(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[2]
        # The actual data have range for row=[1,42] and col=[0,2]
        self.socioecons_dict = self._retrieve_data(range(1, 43), range(0, 3), sheet_name, self._return_sheet(sheet_name))

    def _emissions(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[3]
        # The actual data have range for row=[1,10] and col=[0,1]
        self.emissions_dict = self._retrieve_data(range(1, 11), range(0, 2), sheet_name, self._return_sheet(sheet_name))

    def _policies(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[4]
        # The actual data have range for row=[1,18] and col=[0,2]
        self.policies_dict = self._retrieve_data(range(1, 19), range(0, 3), sheet_name, self._return_sheet(sheet_name))

    def _sdgs(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[5]
        # The actual data have range for row=[1,15] and col=[0,1]
        self.sdgs_dict = self._retrieve_data(range(1, 16), range(0,2), sheet_name, self._return_sheet(sheet_name))

    def _model_info(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[6]
        sheet = self._return_sheet(sheet_name)
        model_title = sheet.cell_value(0, 1)
        # For model name use the Model acronym with no spaces and all char lower
        model_name = "".join(model_title.split()).lower()
        long_title = sheet.cell_value(1, 1)
        long_description = sheet.cell_value(5, 1)
        short_description = sheet.cell_value(2, 1)
        icon = ""
        ordering = ""
        coverage = ""
        partener = sheet.cell_value(3, 1)
        type_of_model = sheet.cell_value(4, 1)
        time_horizon = 0
        time_steps_in_solution = 0
        temp = [model_name, model_title, long_title, partener, type_of_model, time_horizon, time_steps_in_solution,
                long_description,short_description, icon, coverage]
        self.model_dict = {
                            "Model": temp
                                    }


    def _regions(self):
        """

        :return:
        """
        sheet_name = self.sheets_name[7]
        # The number of rows is not fixed, but the range of cols is col=[0,2]
        sheet = self._return_sheet(sheet_name)
        data = []
        row = 1  # The actually data begin from row 1
        while True:
            temp = []
            for col in range(0,3):
                temp.append(sheet.cell_value(row, col))
            if temp[1] == '':  # If the cell which contains the name of country is empty then break the loop
                break
            row += 1
            data.append(temp)
        self.regions_dict = {
                                "Regions": data
                                }

    def return_data(self):
        """

        :return:
        """
        self._regions()
        self._model_info()
        self._sdgs()
        self._policies()
        self._emissions()
        self._socioecons()
        self._mitigationadaptation()
        self._sectors()
        return_dict = {}
        return_dict.update(self.regions_dict)
        return_dict.update(self.model_dict)
        return_dict.update(self.sdgs_dict)
        return_dict.update(self.policies_dict)
        return_dict.update(self.emissions_dict)
        return_dict.update(self.socioecons_dict)
        return_dict.update(self.mitigationadaptation_dict)
        return_dict.update(self.sector_dict)
        return  return_dict




class ImportData:
    def __init__(self, excel_name):
        self.excel_name = excel_name
        self.retrieve_data = Parser(self.excel_name).return_data()

    def _load_model(self):
        """

        :return:
        """
        # First get the latest id and ordering
        latest_id = ModelsInfo.objects.latest('id').id
        latest_ordering = ModelsInfo.objects.latest('ordering').ordering
        new_model = self.retrieve_data["Model"]
        self.new_model_id = max(ModelsInfo.objects.all().values_list('id', flat=True)) + 1
        new_model_ordering = max(ModelsInfo.objects.all().values_list('ordering', flat=True)) + 1
        # At the begin add new id and at index -2 add new ordering
        new_model = [self.new_model_id]+new_model[:-1]+[new_model_ordering]+[new_model[-1]]
        new_model = ModelsInfo(*new_model)
        new_model.save()
        # Return model object
        self.model_obj = ModelsInfo.objects.get(id=self.new_model_id)

    def _load_emissions(self):
        """

        :return:
        """
        new_emissions = self.retrieve_data['Emissions']
        for emission in new_emissions:
            # emission is a list with length equal to two
            # index 0 contains the name of emission
            # index 1 contains the state of emission
            emission_obj = EmissionsName.objects.get(emissions_name=emission[0])
            emission_temp = EmissionsStates(model_id=self.model_obj, state=emission[1], emissions_name_id=emission_obj)
            emission_temp.save()

    def _load_policies(self):
        """

        :return:
        """
        new_policies = self.retrieve_data['Policies']
        for policy in new_policies:
            # policy is a list with length equal to three
            # index 0 contains the category of policy
            # index 1 contains the policy/name
            # index 2 contains the state of policy
            policy_cat_obj = PoliciesCat.objects.get(policies_cat=policy[0])
            policy_name_obj = PoliciesName.objects.get(policies_name=policy[1], policies_cat_id=policy_cat_obj.id)
            policy_temp = PoliciesStates(model_id=self.model_obj, policies_name_id=policy_name_obj, state=policy[-1])
            policy_temp.save()

    def _load_sdgs(self):
        """

        :return:
        """
        new_sdgs = self.retrieve_data['SDGs']
        for sdg in new_sdgs:
            # sdg is list with length equal to two
            # index 0 contains the title of sdg
            # index 1 contains the name of sdg
            # TODO check it
            if sdg[1] != '':
                sdg[0] = sdg[0].replace('$', '§')
                sdg_obj = SdgsCat.objects.get(sdgs_title=sdg[0])
                sdg_temp = SdgsName(sdgs_name=sdg[1], model_id=self.model_obj, sdgs_cat_id=sdg_obj)
                sdg_temp.save()

    def _load_socioecons(self):
        """

        :return:
        """
        new_socioecons = self.retrieve_data['SocioEcon']
        for socioecon in new_socioecons:
            # socioecon is a list with length equal to three
            # index 0 contains the category category of socioeco
            # index 1 contains the socioecon/name category of socioeco
            # index 2 contains the model coverage/state category of socioeco
            socioecon_cat_obj = SocioeconsCat.objects.get(socioecons_cat=socioecon[0])
            socioecon_name_obj = SocioeconsName.objects.get(socioecons_name=socioecon[1], socioecons_cat_id=socioecon_cat_obj.id)
            socioecon_temp = SocioeconsStates(state=socioecon[-1], model_id=self.model_obj,
                                              socioecons_name_id=socioecon_name_obj)
            socioecon_temp.save()

    def _load_sectors(self):
        """

        :return:
        """
        new_sectors = list(filter(lambda x:x[-1]!='',self.retrieve_data['Sectors']))
        # Filter all the sectors which model coverage is equal to No
        new_sectors = list(filter(lambda x:x[-1]!='No', new_sectors))
        for sector in new_sectors:
            # sector is a list with length equal to four
            # index 0 contains the category of sector
            # index 1 contains the subcategory of sector
            # index 2 contains the sector name of sector
            # index 3 contains the sector model coverage of sector
            # If the subcategory is empty define new name as
            # empty_+ sector category
            if sector[1] == '':
                subcat_name = 'empty_{}'.format(sector[0])
            else:
                subcat_name = sector[1]
            sector_subcat_obj = SectorSubCat.objects.get(sector_sub_cat=subcat_name)
            sector_name_obj =SectorName.objects.get(sector_name=sector[2], sector_sub_cat=sector_subcat_obj.id)
            sector_name_obj.model_id.add(self.model_obj)

    def _load_mitigationadaptation(self):
        """

        :return:
        """
        new_mitigationadaptation = list(filter(lambda x:x[-1]!='',self.retrieve_data['MitigationAdaptation']))
        # Filter all the sectors which model coverage is equal to No
        new_mitigationadaptation = list(filter(lambda x: x[-1] != 'No', new_mitigationadaptation))
        # Create two lists one of adaptations and one for mitigations
        adaptations = list(filter(lambda x: x[0] == 'Adaptation', new_mitigationadaptation))
        mitigations = list(filter(lambda x: x[0] != 'Adaptation', new_mitigationadaptation))
        for adaptation in adaptations:
            # adaptation is a list with length equal to four
            # index 0 contains the category of adaptation
            # index 1 contains the subcategory of adaptation
            # index 2 contains the name of adaptation
            # index 3 contains the model coverage of adaptation
            adaptation_name_obj = AdaptationName.objects.get(adaptation_name=adaptation[2])
            adaptation_name_obj.model_id.add(self.model_obj)
        for mitigation in mitigations:
            # mitigation is a list with length equal to four
            # index 0 contains the category of mitigation
            # index 1 contains the subcategory of mitigation
            # index 2 contains the name of mitigation
            # index 3 contains the model coverage of mitigation
            mitigation_cat_obj = MitigationsCat.objects.get(mitigations_cat=mitigation[0])
            mitigation_subcat_obj = MitigationsSubCat.objects.get(mitigations_sub_cat=mitigation[1], mitigations_cat_id=mitigation_cat_obj.id)
            mitigation_name_obj = MitigationsName.objects.get(mitigations_name=mitigation[2], mitigations_sub_cat_id =mitigation_subcat_obj.id,)
            mitigation_name_obj.model_id.add(self.model_obj)

    def _load_regions(self):
        """

        :return:
        """
        new_regions = self.retrieve_data['Regions']
        """
        How we get the regions?
        1st case
        The user input the region only ones. In that case loop until find another region name, until then all countries
        belong to first metion region
        2nd case
        User write each time the name of region. Again the countries until find another region name belong to the first
        one
        How we named the new entry region?
        Because possible we would have cases which there are two regions with same name, but they are included different
        countries, the name of region would be,
        given name, without spaces and all char lowercase follow by _<name of model which belong>
        """
        temp_region = None
        countries_list = []
        for k,region in enumerate(new_regions):
            # region is a list with length equal to three
            # 0 index contains region
            # 1 index contains country name
            # 2 index contains country code
            region_name = region[0]
            country_name = region[1]
            country_code = region[2]
            if temp_region is None:
                temp_region = region_name
            if region_name == "" or region_name == temp_region:
                # Load country to countries_list
                countries_list.append([country_name, country_code])
            if region_name != "" and region_name != temp_region or k+1 == len(new_regions):
                """
                End of the region.
                Load the previous region in db, give new value to temp_region and empty countries_list
                """
                # Create the name of the region
                new_region_name = "".join(temp_region.split()).lower() + "_" + self.model_obj.model_name
                # The descr contains all countries names of countries_list
                descr = ",".join(list(map(lambda x: x[0], countries_list)))
                # Save the region
                region_obj = Regions(region_name=new_region_name, region_title=temp_region, descr=descr)
                region_obj.save()
                region_obj.model_name.add(self.model_obj)
                # Save the countries
                for country_list in countries_list:
                    temp_country_name, temp_country_code = country_list
                    # First check if the country is exist, use country code
                    if Countries.objects.filter(country_code=country_code).exists():
                        # if exist get the first object, there is a case which country exist more than ones in db
                        country_obj = Countries.objects.filter(country_code=temp_country_code).first()
                    else:
                        country_obj = Countries(country_name=temp_country_name, country_code=temp_country_code)
                        country_obj.save()
                    country_obj.region_name.add(region_obj)
                # Set new temp_region and countries_list
                temp_region = region_name
                countries_list = [[country_name, country_code]]

    def import_to_db(self):
        """

        :return:
        """
        self._load_model()
        print("LOAD MODEL")
        self._load_regions()
        print("LOAD REGIONS")
        self._load_emissions()
        print("LOAD EMISSION")
        self._load_policies()
        print("LOAD POLICIES")
        self._load_sdgs()
        print("LOAD SDGS")
        self._load_socioecons()
        print("LOAD SOCIOECONS")
        self._load_sectors()
        print("LOAD SECTORS")
        self._load_mitigationadaptation()
        print("LOAD MITIGATIONS ADAPTATION")
