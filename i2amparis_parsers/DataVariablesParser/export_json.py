import xlrd
from i2amparis_main.models import *
from django.apps import apps
from time import sleep


def export_json(path, table_name="ResultsComp", parse=True, sheet=0, given_row=-1):
	"""
	The given excel must have the format of given example excel
	Model name MUST be already exist in django model DataVariablesModels, otherwise script will crash
	:param path: Give the path of the excel
	:param parse: If is True parse data otherwise do not
	:param sheet: Give the number of sheet which include the data, start by zero(0)
	:param table_name: The name of table where we want to parse our data
	:param given_row: In case somethings goes wrong in parse put the last row which have been parsed
	:return: A dict with scenarios, regions, variable and units which doesnt exist in our database
	"""
	doesnt_exist_dict = {}
	b = xlrd.open_workbook(path)
	s = b.sheet_by_index(sheet)
	# checkTitlesFirstRow(s)
	checkForModel(s)  # Check if given models there are in our database, otherwise raise exception
	checkForEmptyRows(s)  # Check if in first five cols there is empty row, otherwise raise exception
	checkForStringsInValues(s)
	sleep(20)
	models = s.col_values(0)[1:]
	models_unq = list(set(s.col_values(0)[1:]))
	scenarios = s.col_values(1)[1:]
	scenarios_unq = list(set(s.col_values(1)[1:]))
	regions = s.col_values(2)[1:]
	regions_unq = list(set(s.col_values(2)[1:]))
	variables = s.col_values(3)[1:]
	variables_unq = list(set(s.col_values(3)[1:]))
	# units = s.col_values(4)[1:]
	units_unq = list(set(s.col_values(4)[1:]))
	years = [int(x) for x in s.row_values(0)[5:]]
	data = {}
	sc_dict = {}
	# TODO fill table scenarios, regions,variables and units
	all_comp = []
	# TODO check if already exist
	ss_doesnt_exist = []
	for ss in scenarios_unq:
		ss = ss.strip()
		if not ScenariosRes.objects.filter(title=ss).exists():
			ss_doesnt_exist.append(ss)
			print("Scenario:{} doesnt exist".format(ss))
			if parse:
				t_sc = ScenariosRes.objects.create(title=ss.strip(), name=ss.strip())
				t_sc.save()
	doesnt_exist_dict['Scenarios'] = ss_doesnt_exist
	r_doesnt_exist = []
	for r in regions_unq:
		r = r.strip()
		# if not RegionsRes.objects.filter(title=r).exists():
		if not RegionsRes.objects.filter(name=r).exists():
			r_doesnt_exist.append(r)
			print("Region:{} doesnt exist".format(r))
			if parse:
				if Countries.objects.filter(country_code=r.strip()).exists():
					country_name = Countries.objects.get(country_code=r.strip()).country_name
					t_re = RegionsRes.objects.create(title=country_name, name=r.strip())
				else:
					t_re = RegionsRes.objects.create(title=r.strip(), name=r.strip())
				t_re.save()
	doesnt_exist_dict['Regions'] = r_doesnt_exist
	u_doesnt_exist = []
	for u in units_unq:
		if not UnitsRes.objects.filter(title=u.strip()).exists():
			u_doesnt_exist.append(u)
			print("Unit:{} doesnt exist".format(u))
			if parse:
				t_un = UnitsRes.objects.create(title=u.strip(), name=u.strip())
				t_un.save()
	doesnt_exist_dict['Units'] = u_doesnt_exist
	v_doesnt_exist = []
	for v in variables_unq:
		v = v.strip()
		if not VariablesRes.objects.filter(title=v).exists():
			v_doesnt_exist.append(v)
			print("Variable:{} doesnt exist".format(v))
			if parse:
				t_var = VariablesRes.objects.create(title=v, name=v)
				t_var.save()
	doesnt_exist_dict['Variables'] = v_doesnt_exist
	# print(doesnt_exist_dict)
	# sleep(20)
	no_empty_rows = 0
	empty_rows = 0
	sum_of_rows = len(models)
	for r in range(1, len(models) + 1):
		if r > given_row:
			"In case something goes wrong you now the row where parse stoped"
			# print("ROW IN EXCEL----->", r+1)  # If you want to start from e.g 400 must parse arg 399
			row = s.row_values(r)
			print(row[:5])
			model, scenario, region, variable, unit = row[:5]
			if type(model) == type(42.0):
				model = '42'
			if parse:
				m = DataVariablesModels.objects.get(title=model.strip())
				sc = ScenariosRes.objects.get(title=scenario.strip())
				re = RegionsRes.objects.get(name=region.strip())
				var = VariablesRes.objects.get(title=variable.strip())
				un = UnitsRes.objects.get(title=unit.strip())
			for k, year in enumerate(years):
				val = row[5+k]
				if type(val) == int or type(val) == float:
					no_empty_rows += 1
					# If val is number int or float parset it otherwise ignore it
					print(f"Model:{model}, Scenario:{scenario}, Region:{region}, Variable:{variable}, Unit:{unit},"
						  f" Year:{year}, Value:{val}. Row in excel {r+1}. Complete:{round((100*r)/sum_of_rows,2)}%")
					if parse:
						temp_table = apps.get_model('i2amparis_main', table_name)
						temp = temp_table(model=m, scenario=sc, region=re, variable=var, unit=un, year=year, value=val)
						temp.save()
				else:
					empty_rows += 1
	# print(doesnt_exist_dict)
	final_report(doesnt_exist_dict, empty_rows, no_empty_rows)


def final_report(d, erow,nerow):
	"""
	:param d:
	:param erow:
	:param nerow:
	:return:
	"""
	print(f"File has {erow} empty cells")
	print(f"File has {nerow} not empty cells, which parsed in database")
	if len(d['Scenarios']) != 0:
		print(f"File has {len(d['Scenarios'])} new scenario(s) which are {d['Scenarios']}")
	else:
		print("File  doesn't have any new Scenarios")
	if len(d['Regions']) != 0:
		print(f"File has  {len(d['Regions'])} new region(s) which are {d['Regions']}")
	else:
		print("File  doesn't have any new Regions")
	if len(d['Variables']) != 0:
		print(f"File has {len(d['Variables'])} new variable(s) which are {d['Variables']}")
	else:
		print("File  doesn't have any new Variables")
	if len(d['Units']) != 0:
		print(f"File has {len(d['Units'])} new unit(s)  which are {d['Units']}")
	else:
		print("File  doesn't have any new Units")


def checkForModel(sheet):
	"""
	Check if given models exist in our database.
	In they doesnt raise exception
	:param sheet:Object sheet
	:return:
	"""
	print("Check if given models exist in DataVariablesModels")
	model = sheet.col_values(0)[1:]
	model = list(map(lambda x: case42(x), model))
	m = [i for i in set(model) if not DataVariablesModels.objects.filter(title=i.strip()).exists()]
	default_models = list(DataVariablesModels.objects.values_list('title', flat=True).all())
	if len(m) != 0:
		raise Exception(f"Given models:{m} doesnt exist in our Database. The models can be anyone from this list "
						f"{default_models}")


def case42(m):
	"In case given model is number 42 return 42 as string"
	if m == 42:
		return '42'
	else:
		return m

def checkForEmptyRows(sheet):
	"""
	Check if first five cols have empty or not string rows, in case there is empty row raise exception
	:param sheet:Object sheet
	:return:
	"""
	print("Check for empty rows in first five columns")
	d = {}
	for col, name in enumerate(["Model", "Scenario", "Region", "Variable", "Unit"]):
		l = sheet.col_values(col)
		if col == 0:
			"Convert model 42 to string"
			l = list(map(lambda x: case42(x), l))
		empty = [k+1 for k, i in enumerate(l) if i.isspace() or i == '' or type(i) != str]  # Add 1 to k to have the index in excel
		if len(empty) != 0:
			d[name] = empty
	if d != {}:
		raise Exception(f"There are empty fields:{d}")

def checkForStringsInValues(sheet):
	print("Check if in area of values there is any no empty string, if string is empty space ignore it")
	first_row = sheet.row_values(0)[5:]
	d = {}
	for k, year in enumerate(first_row):
		l = [j for j, val in enumerate(sheet.col_values(k+5)[1:]) if isNotEmptyStr(val)]
		if len(l) != 0:
			d[year] = l
	if d != {}:
		raise Exception(f"There are strings in values: {d}")

def isNotEmptyStr(s):
	if type(s) == str:
		if s.isspace() or s == "":
			return False
		else:
			return True


def checkTitlesFirstRow(sheet):
	print("Check if first row of sheet has the requirement fields in the right order")
	t = ['Model', 'Scenario', 'Region', 'Variable', 'Unit', '2005', '2010', '2015', '2020',
		 '2025', '2030', '2035', '2040', '2045', '2050', '2055', '2060', '2065', '2070', '2075', '2080', '2085', '2090',
		 '2095', '2100']
	if sheet.row_values(0) != t:
		raise Exception(f"There is something wrong with titles. Titles must be in this order{t}")