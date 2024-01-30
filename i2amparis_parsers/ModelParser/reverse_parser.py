from i2amparis_main.models import *
import openpyxl as xl


def write_cell(sheet, answer_exists, sheet_row, column):
    if answer_exists:
        book[sheet][column + str(sheet_row)] = 'Yes'
    else:
        book[sheet][column + str(row)] = 'No'


models = ModelsInfo.objects.all()

for model in models:
    print(f'{model}')
    book = xl.load_workbook('models_xls\\template.xlsx')

    book['Model_Info']['B1'] = model.model_title
    book['Model_Info']['B2'] = model.long_title
    book['Model_Info']['B3'] = model.short_description
    book['Model_Info']['B4'] = model.partener
    book['Model_Info']['B5'] = model.type_of_model
    book['Model_Info']['B6'] = model.long_description

    for row in range(2, 12):
        emission = EmissionsStates.objects.filter(emissions_name_id__emissions_name=book['Emissions']['A' + str(row)].value,
                                                  model_id=model)
        if emission:
            book['Emissions']['B' + str(row)] = emission[0].state

    for row in range(2, 62):
        exists = SectorName.objects.filter(sector_name=book['Sectors']['C' + str(row)].value,
                                           sector_sub_cat__sector_cat_id__sector_cat=book['Sectors']['A' + str(row)].value,
                                           model_id=model)
        write_cell('Sectors', exists, row, 'D')

    for row in range(2, 107):
        if row < 17 or row > 49:
            exists = MitigationsName.objects.filter(mitigations_name=book['MitigationAdaptation']['C' + str(row)].value,
                                                    mitigations_sub_cat_id__mitigations_cat_id__mitigations_cat=book['MitigationAdaptation']['A' + str(row)].value,
                                                    model_id=model)
        else:
            exists = MitigationsName.objects.filter(mitigations_name=book['MitigationAdaptation']['C' + str(row)].value,
                                                    mitigations_sub_cat_id__mitigations_sub_cat=book['MitigationAdaptation']['B' + str(row)].value,
                                                    mitigations_sub_cat_id__mitigations_cat_id__mitigations_cat=book['MitigationAdaptation']['A' + str(row)].value,
                                                    model_id=model)
        write_cell('MitigationAdaptation', exists, row, 'D')

    for row in range(2, 44):
        socioecon = SocioeconsStates.objects.filter(socioecons_name_id__socioecons_name=book['SocioEcon']['B' + str(row)].value,
                                                                            socioecons_name_id__socioecons_cat_id__socioecons_cat=book['SocioEcon']['A' + str(row)].value,
                                                                            model_id=model)
        if socioecon:
            book['SocioEcon']['C' + str(row)] = socioecon[0].state

    regions = Regions.objects.filter(model_name=model)
    region_row = 2
    for region in regions:
        countries = Countries.objects.filter(region_name=region)
        for i, country in enumerate(countries):
            book['Regions']['A' + str(i + region_row)] = region.region_title
            book['Regions']['B' + str(i + region_row)] = country.country_name
            book['Regions']['C' + str(i + region_row)] = country.country_code
        region_row += len(countries)

    for row in range(2, 17):
        sdgs_cat = SdgsName.objects.filter(sdgs_cat_id__sdgs_title=book['SDGs']['A' + str(row)].value,
                                           model_id=model)

        if sdgs_cat:
            book['SDGs']['B' + str(row)] = sdgs_cat[0].sdgs_name
        else:
            book['SDGs']['B' + str(row)] = 'none'

    for row in range(2, 20):
        policy = PoliciesStates.objects.filter(policies_name_id__policies_name=book['Policies']['B' + str(row)].value,
                                               policies_name_id__policies_cat_id__policies_cat=book['Policies']['A' + str(row)].value,
                                               model_id=model)
        if policy:
            book['Policies']['C' + str(row)] = policy[0].state

    book.save(f'models_xls\\{model}.xlsx')