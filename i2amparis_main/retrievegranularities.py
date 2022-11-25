from i2amparis_main.models import *


class RetrieveGranularities:
    def __init__(self, model_id):
        # self.model_id = ModelsInfo.objects.get(model_name=model_name).id
        self.model_id = model_id
        self.data = {
            'MitigationAdaptationMeasures': self.mitigationadaptation(),
            'Sectors': self.sectors(),
            'SDGs': self.sdgs(),
            'Emissions': self.emissions(),
            'Policy': self.policies(),
            'SocioEconomics': self.socioecons()
        }

    def create_name_list(self, names, names_enable):
        """
        return a list of dict, key name val bool
        """
        return list(map(lambda x: {x: True} if x in names_enable else {x: False}, names))

    def create_simple_list(self, data, cat=None):
        """
        param data: Is the output of create_name_list, which is a list of dicts
        return : a string which is a simple html list
        """
        color_dict = {
            True: '#97ae21',
            False: 'grey'
        }
        decor_dict = {
            True: 'none',
            False: 'line-through'
        }
        temp_list = []
        for i in data:
            [[k, v]] = i.items()
            temp = '<li style="color:{}; text-decoration:{}"> {} </li> '.format(color_dict[v], decor_dict[v], k)
            temp_list.append(
                temp
            )
        output = '<ul> {} </ul>'.format(''.join(temp_list))
        if cat is not None:
            output = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4> {}'.format(cat, output)
        return output

    def create_nested_list(self, data, cat):
        # First must add at the begin of the list the title of category
        subs = list(data.keys())
        if len(subs) == 1:
            if subs[0] == '':
                output = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4> {}'.format(cat, data['']['names_html'])
            else:
                output = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4><ul> <li>{}</li> {}</ul>'.\
                    format(cat, subs[0], data)
        else:
            temp_list = []
            for sub in subs:
                temp = '<li>{}</li>{}'.format(sub, data[sub]['names_html'])
                temp_list.append(temp)
            temp_html = '<ul>{}</ul>'.format(''.join(temp_list))
            output = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4> {}'.format(cat, temp_html)
        return output

    def mitigationadaptation(self):
        """

        """
        adataptation_dict = {}
        for cat in AdaptationCat.objects.all().values_list('adaptation_cat', flat=True):
            # Adaptation has only one category
            cat_id = AdaptationCat.objects.get(adaptation_cat=cat).id
            cat_icon = AdaptationIcon.objects.get(adaptation_cat_id=cat_id).adaptation_icon
            names = AdaptationName.objects.filter(adaptation_cat_id=cat_id).values_list('adaptation_name', flat=True)
            names_enable = AdaptationName.objects.filter(
                adaptation_cat_id=cat_id, model_id=self.model_id).values_list('adaptation_name', flat=True)
            names_list_dict = self.create_name_list(names, names_enable)
            if len(names_enable) > 0:
                enable_adaptation = True
                html = self.create_simple_list(names_list_dict, cat)
            else:
                enable_adaptation = False
                html = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4>'.format(cat)

            adataptation_dict.update({
                cat: {
                    'names': names_list_dict,
                    'icon': cat_icon,
                    'is_enable': 'green' if enable_adaptation else 'grey',
                    'html': html
                }
            })
        mitigation_dict = {}
        for cat in MitigationsCat.objects.all().values_list('mitigations_cat', flat=True).order_by('ordering'):
            cat_id = MitigationsCat.objects.get(mitigations_cat=cat).id
            cat_icon = MitigationsIcon.objects.get(mitigation_cat_id=cat_id).mitigation_icon
            subscat_dict = {}
            enable = False
            for subcat in MitigationsSubCat.objects.filter(mitigations_cat_id=cat_id).values_list('mitigations_sub_cat', flat=True):
                subcat_id = MitigationsSubCat.objects.get(mitigations_sub_cat=subcat, mitigations_cat_id=cat_id).id
                names = MitigationsName.objects.filter(mitigations_sub_cat_id=subcat_id).values_list('mitigations_name', flat=True)
                names_enable = MitigationsName.objects.filter(mitigations_sub_cat_id=subcat_id, model_id=self.model_id).values_list('mitigations_name', flat=True)
                names_list_dict = self.create_name_list(names, names_enable)
                if enable == False:
                    if len(names_enable) > 0:
                        enable = True
                subscat_dict.update({
                    subcat: {
                        'names': names_list_dict,
                        'names_html': self.create_simple_list(names_list_dict)
                    }
                })
            if enable:
                html = self.create_nested_list(subscat_dict, cat)
            else:
                html = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4>'.format(cat)
            mitigation_dict.update({
                cat: {
                    'subs': subcat,
                    'icon': cat_icon,
                    'is_enable': 'green' if enable else 'grey',
                    'html': html
                }
            })
        # mitigationadaptation_dict = {
        #     'adaptation': adataptation_dict,
        #     'mitigation': mitigation_dict
        # }
        mitigationadaptation_dict = {}
        mitigationadaptation_dict.update(mitigation_dict)
        mitigationadaptation_dict.update(adataptation_dict)
        return mitigationadaptation_dict


    def sectors(self):
        sectors_dict = {}
        for cat in SectorCat.objects.all().values_list('sector_cat', flat=True).order_by('ordering'):
            cat_id = SectorCat.objects.get(sector_cat=cat).id
            cat_icon = SectorIcon.objects.get(sector_cat_id=cat_id).sector_icon
            subcat_dict = {}
            enable = False
            # Subcat in some cases is empty string
            for subcat in SectorSubCat.objects.filter(sector_cat_id=cat_id).values_list('sector_sub_cat', flat=True):
                subcat_id = SectorSubCat.objects.get(sector_sub_cat=subcat).id
                names = SectorName.objects.filter(sector_sub_cat=subcat_id).values_list('sector_name', flat=True).order_by('ordering')
                names_enable = SectorName.objects.filter(sector_sub_cat=subcat_id, model_id=self.model_id).values_list('sector_name', flat=True)
                names_list_dict = self.create_name_list(names, names_enable)
                # names_html = ''
                if enable == False:
                    # Check if cat is enable, it is if at least one time the names_enable > 0
                    if len(names_enable) > 0:
                        enable = True
                        # names_html = self.create_simple_list(names_list_dict)
                    if subcat.startswith('empty_'):
                        subcat = ''
                subcat_dict.update({
                    subcat: {
                        'names': names_list_dict,
                        'names_html': self.create_simple_list(names_list_dict)
                    }
                })
            if enable:
                html = self.create_nested_list(subcat_dict, cat)
            else:
                html = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4>'.format(cat)
            sectors_dict.update({
                cat: {
                    'subs': subcat_dict,  # There is the case of empty subcategory
                    'icon': cat_icon,
                    'is_enable': 'green' if enable else 'grey',
                    'html': html
                }
            })
        return sectors_dict

    def sdgs(self):
        # TODO check the final order of sdgs_dict
        sdgs_dict = {}
        for cat in SdgsCat.objects.all().order_by('ordering').values_list('sdgs_cat', flat=True).order_by('ordering'):
            cat_id = SdgsCat.objects.get(sdgs_cat=cat).id
            cat_title = SdgsCat.objects.get(sdgs_cat=cat).sdgs_title
            cat_icon = SdgsIcon.objects.get(sdgs_cat_id=cat_id).sdgs_icon
            name = list(SdgsName.objects.filter(sdgs_cat_id=cat_id, model_id=self.model_id).values_list('sdgs_name', flat=True))
            if len(name) > 0:
                # We suppose the sdgs all the time have only one name, so if len is >0 will be 1 and we get the name[0]
                html = '<h4 style="padding:5px;margin-bottom:5px"> {}</h4>  <p style="margin-left:1em">{}</p> '.format(cat_title, name[0])
                enable = True
            else:
                html = '<h4 style="padding:5px;margin-bottom:5px"> {}</h4>'.format(cat)
                enable = False
            sdgs_dict.update({
                cat: {
                    'name': name,
                    'icon': cat_icon,
                    'title': cat_title,
                    'is_enable': 'green' if enable else 'grey',
                    'html': html
                }
            })
        # TODO order the elements of dict base to number in title
        return sdgs_dict

    def emissions(self):
        emissions_dict = {}
        for name in EmissionsName.objects.all().values_list('emissions_name', flat=True).order_by('ordering'):
            enable = False
            name_id = EmissionsName.objects.get(emissions_name=name).id
            name_icon = EmissionsIcon.objects.get(emission_name=name_id).emissions_icon_name
            # TODO states can be more than one
            states = EmissionsStates.objects.filter(model_id=self.model_id, emissions_name_id=name_id).values_list('state', flat=True)
            temp_list = []
            for state in states:
                if state != 'Not represented':
                    temp = '<li>{}</li>'.format(state)
                    temp_list.append(temp)
            if len(temp_list) > 0:
                temp_html = '<ul>{}</ul>'.format(''.join(temp_list))
                name_html = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4> {}'.format(name, temp_html)
                enable = True
            else:
                name_html = '<h4 style="text-align:center;padding:5px;margin-bottom:5px"> {} </h4>'.format(name)
            emissions_dict.update({
                name: {
                    'icon': name_icon,
                    'html': name_html,
                    'is_enable': 'green' if enable else 'grey'
                }
            })
        return emissions_dict

    def policies(self):
        policies_dict = {}
        for cat in PoliciesCat.objects.all().values_list('policies_cat', flat=True).order_by('ordering'):
            cat_id = PoliciesCat.objects.get(policies_cat=cat).id
            cat_icon = PoliciesIcon.objects.get(policies_cat=cat_id).policies_icon
            names_state = []
            enable = False
            for name in PoliciesName.objects.filter(policies_cat_id=cat_id).values_list('policies_name', flat=True):
                name_id = PoliciesName.objects.get(policies_name=name, policies_cat_id=cat_id).id
                states = list(PoliciesStates.objects.filter(policies_name_id=name_id, model_id=self.model_id).values_list('state', flat=True))
                if len(states) > 0:
                    # if states[0] in ['Feasible', 'Feasible with modifications']:
                    temp_state = set(states) & set(['Feasible', 'Feasible with modifications'])
                    if len(temp_state) > 0:
                        state = True
                    else:
                        # In this case if there is a another option than  'Feasible' or 'Feasible with modifications' is false
                        # TODO is this correct?
                        state = False
                else:
                    # If we have more than one states state will be true
                    state = False
                if enable == False:
                    if state:
                        enable = True
                names_state.append(
                    {name: state}
                )
            policies_dict.update({
                cat: {
                    'icon': cat_icon,
                    'names': names_state,
                    'html': self.create_simple_list(names_state, cat),
                    'is_enable': 'green' if enable else 'grey'
                }
            })
        return policies_dict

    def socioecons(self):
        """

        """
        socioecons_dict = {}
        for cat in SocioeconsCat.objects.all().values_list('socioecons_cat', flat=True).order_by('ordering'):
            cat_id = SocioeconsCat.objects.get(socioecons_cat=cat).id
            cat_icon = SocioeconsIcon.objects.get(socioecons_cat_id=cat_id).socioecons_icons
            names_state = []
            enable = False
            for name in SocioeconsName.objects.filter(socioecons_cat_id=cat_id).values_list('socioecons_name', flat=True):
                name_id = SocioeconsName.objects.get(socioecons_name=name, socioecons_cat_id=cat_id).id
                states = SocioeconsStates.objects.filter(
                    model_id=self.model_id, socioecons_name_id=name_id).values_list('state', flat=True)
                if len(states) > 0:
                    temp_states = set(states) & set(['Endogenous', 'Exogenous'])
                    if len(temp_states) > 0:
                        state = True
                    # if states[0] in ['Endogenous', 'Exogenous']:
                    #     state = True
                    else:
                        # In this case if there is a another option than  'Endogenous' or 'Exogenous' is false
                        # TODO is this correct?
                        state = False
                else:
                    # In case there is more than one state is true
                    state = False
                if enable == False:
                    if state:
                        enable = True
                names_state.append(
                    {name: state}
                )
            socioecons_dict.update({
                cat: {
                    'names': names_state,
                    'html': self.create_simple_list(names_state, cat),
                    'icon': cat_icon,
                    'is_enable': 'green' if enable else 'grey'
                }
            })
        return socioecons_dict








