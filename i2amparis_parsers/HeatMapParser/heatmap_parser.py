from i2amparis_main.models import *
import xlrd


class HeatMapParser:
	def __init__(self, f, f_units):
		self.f = f  # The path of file
		self.f_units = f_units  # The path of file for units
		self.harmdatanew_dict = {}
		self.dict_convert = {
					1: 'Extractable model output',
					2: 'Not harmonized',
					3: 'Fully Harmonised',
					4: 'Partially harmonised',
					5: 'Checked for consistency',
					6: 'Not represented in model'
					}
		self.open_file()
		self.open_file_units()

	def open_file(self):
		book = xlrd.open_workbook(self.f)
		# self.sheet_heatmap = book.sheet_by_index(0)
		self.sheet_heatmap = book.sheet_by_name('updated map')
		# self.sheet_timespan = book.sheet_by_index(1)
		self.sheet_timespan = book.sheet_by_name('timespan')
		self.sheet_sources = book.sheet_by_index(2)
		self.sheet_links = book.sheet_by_index(3)

	def open_file_units(self):
		book = xlrd.open_workbook(self.f_units)
		self.sheet_units = book.sheet_by_index(4)

	def create_row_col_dict(self, sheet):
		models_row = sheet.row_values(1)
		variables_cols = sheet.col_values(1)[:-15]
		models_dict = self.loop_lst(models_row)
		variables_dict = self.loop_lst(variables_cols)
		return models_dict, variables_dict

	def loop_lst(self, data):
		temp = {}
		for k, i in enumerate(data):
			if i != '':
				if i == 42.0:
					i = '42'
				temp[i] = k
		return temp

	def read_tab_heatmap(self):
		models_dict, variables_dict = self.create_row_col_dict(self.sheet_heatmap)
		from pprint import pprint as pp
		pp(models_dict)
		pp(variables_dict)
		for model, y in models_dict.items():
			temp = {}
			for variable, x in variables_dict.items():
				print("X:{}, Y:{}, VAL:{}".format(x, y, self.sheet_heatmap.cell_value(x, y)))
				val = int(self.sheet_heatmap.cell_value(x, y))
				# print("Model:{}, variable:{}, value:{}".format(model, variable, val))
				temp[variable] = {"io_status": self.dict_convert[val]}
			self.harmdatanew_dict[model] = temp

	def parser_heatmap_to_db(self, model_name, var_name, val_txt):
		model = DataVariablesModels.objects.get(title=model_name)
		var = DataVariablesHarmonisation.objects.get(title=var_name)
		# DatasetVariableHarmonisation.objects.create(harmonisation_model=model, harmonisation_variable=var,
		# 											harmonisation_io_status=val_txt).save()

	def read_tab_timespan(self):
		models_dict, variables_dict = self.create_row_col_dict(self.sheet_timespan)
		for model, y in models_dict.items():
			for variable, x in variables_dict.items():
				val = self.sheet_timespan.cell_value(x, y)
				print("TIME:{}".format(val))
				if type(val) == type(1.0):
					val = str(int(val))
				if val != '':
					print("TIMESPAN--->Model:{} Variable:{} Value:{}".format(model, variable, val))
					self.harmdatanew_dict[model][variable]["var_timespan"] = val

	# def read_tab_sources(self):
	# 	models_dict, variables_dict = self.create_row_col_dict(self.sheet_sources)
	# 	for model, y in models_dict.items():
	# 		for variable, x in variables_dict.items():
	# 			val = self.sheet_sources.cell_value(x, y)
	# 			if val != '':
	# 				# print("Model:{} Variable:{} Value:{}".format(model, variable, val))
	# 				self.harmdatanew_dict[model][variable]["var_source_info"] = val
	# 
	# 
	# def read_tab_links(self):
	# 	models_dict, variables_dict = self.create_row_col_dict(self.sheet_links)
	# 	for model, y in models_dict.items():
	# 		for variable, x in variables_dict.items():
	# 			val = self.sheet_links.cell_value(x, y)
	# 			if val != '':
	# 				# print("Model:{} Variable:{} Value:{}".format(model, variable, val))
	# 				self.harmdatanew_dict[model][variable]["var_source_url"] = val

	def read_tabs_sources_links(self):
		models_dict_sources, _ = self.create_row_col_dict(self.sheet_sources)
		variables_sources = self.sheet_sources.col_values(1)[2:]
		variables_dict = {}
		for k, i in enumerate(variables_sources):
			variables_dict[k] = i
		self.variables_dict_ranges = {}
		temp_var = variables_dict[0]
		temp_idx = 0
		# TODO need to check if the last variable has more than one sources/links
		for k, v in variables_dict.items():
			if v != '':
				if temp_idx != k-1:
					self.variables_dict_ranges[temp_var] = [temp_idx, k-1]
				else:
					self.variables_dict_ranges[temp_var] = [temp_idx]
				temp_var = v
				temp_idx = k
		for model, y in models_dict_sources.items():
			for variable, range_lst in self.variables_dict_ranges.items():
				temp_dict = {}
				if len(range_lst) > 1 and range_lst[-1] - range_lst[0] > 1:
					begin,end = range_lst
					for i in range(begin, end):
						if self.sheet_sources.cell_value(i+2,y) != '':
							temp_dict[self.sheet_sources.cell_value(i+2,y)] = self.sheet_links.cell_value(i+2,y)
				elif len(range_lst) == 1:
					temp_idx_var = range_lst[0]
					if self.sheet_sources.cell_value(temp_idx_var + 2, y) != '':
						temp_dict[self.sheet_sources.cell_value(temp_idx_var + 2, y)] = self.sheet_links.cell_value(temp_idx_var + 2, y)
				else:
					for temp_i in range_lst:
						if self.sheet_sources.cell_value(temp_i + 2, y) != '':
							temp_dict[self.sheet_sources.cell_value(temp_i + 2, y)] = self.sheet_links.cell_value(temp_i + 2, y)
				self.harmdatanew_dict[model][variable]["var_source_and_links"] = temp_dict

	def read_source_links(self):
		b = xlrd.open_workbook(self.f)
		source_titles = b.sheet_by_name('source_titles')
		source_links = b.sheet_by_name('source_links')
		general_source_titles = b.sheet_by_name('general_source_titles')
		models_dict_sources, _ = self.create_row_col_dict(source_titles)
		variables = source_titles.col_values(1)[2:]
		variables_dict = {}
		for k, i in enumerate(variables):
			variables_dict[k] = i
		variables_dict_ranges = {}
		temp_var = variables_dict[0]
		temp_idx = 0
		# TODO need to check if the last variable has more than one sources/links
		# max_col = max(list(map(lambda x: len(source_titles.col_values(x)), list(models_dict_sources.values()))))
		# print("MAX:{}".format(max_col))
		for k, v in variables_dict.items():
			if v != '':
				if temp_idx != k-1:
					variables_dict_ranges[temp_var] = [temp_idx, k-1]
				else:
					variables_dict_ranges[temp_var] = [temp_idx]
				temp_var = v
				temp_idx = k
			if k == len(variables) -1:
				# variables_dict_ranges[temp_var] = [temp_idx, max_col]
				variables_dict_ranges[temp_var] = [temp_idx]
		data = {}
		for model, y in models_dict_sources.items():
			temp_var_dict = {}
			for var, rnge in variables_dict_ranges.items():
				temp_val_dict = {}
				if len(rnge) > 1 and rnge[1] > rnge[0]:
					rnge = [i for i in range(rnge[0],rnge[1]+1)]
				else:
					rnge = [rnge[0]]
				for x in rnge:
					val = source_titles.cell_value(x+2, y)
					title = general_source_titles.cell_value(x+2, y)
					url = source_links.cell_value(x+2, y)
					if val != '':
						# print("Model:{}, Var:{}, Value:{}, Title:{}, URL:{}".format(model, var, val, title, url))
						temp_val_dict[val] = {'title': title, 'url': url}
				if temp_val_dict != {}:
					self.harmdatanew_dict[model][var]["var_source_and_links"] = temp_val_dict
			# 		temp_var_dict[var] = temp_val_dict
			# if temp_var_dict != {}:
			# 	data[model] = temp_var_dict
		# return data



	def read_tab_units(self):
		models = self.sheet_units.row_values(1)
		variables = self.sheet_units.col_values(2)
		models_dict = {}
		variables_dict = {}
		for k, model in enumerate(models):
			if model != '':
				if model == 42.0:
					model = '42'
				models_dict[model] = k
		for kk, variable in enumerate(variables):
			if variable != '':
				variables_dict[variable] = kk
		for model, y in models_dict.items():
			for variable, x in variables_dict.items():
				val = self.sheet_units.cell_value(x, y)
				# print("X:{}, Y:{}".format(x,y))
				if val != '':
					# print("Model:{} Variable:{} Value:{}".format(model, variable, val))
					self.harmdatanew_dict[model][variable]["var_unit"] = val


	def parser_to_hamrdatanew(self):
		self.read_tab_heatmap()
		self.read_tab_timespan()
		self.read_tab_units()
		self.read_source_links()
		# self.read_tabs_sources_links()
		# Dont insert GCAM-USA
		del self.harmdatanew_dict['GCAM-USA']
		for model in self.harmdatanew_dict:
			for variable in self.harmdatanew_dict[model]:
				print("model:{}, variable:{}".format(model, variable))
				model_id = DataVariablesModels.objects.get(title=model)
				variable_id = Harmonisation_Variables.objects.get(var_title=variable)
				HarmDataNew.objects.create(
											model=model_id, variable=variable_id,
											io_status=self.harmdatanew_dict[model][variable].get("io_status", ""),
											var_unit=self.harmdatanew_dict[model][variable].get("var_unit", ""),
											var_timespan=self.harmdatanew_dict[model][variable].get("var_timespan", "")
											).save()
				if self.harmdatanew_dict[model][variable].get('var_source_and_links', None):
					for source, source_dict in self.harmdatanew_dict[model][variable]['var_source_and_links'].items():
						title = source_dict['title']
						if HarmDataSourcesTitles.objects.filter(title=title).exists():
							title_obj = HarmDataSourcesTitles.objects.get(title=title)
						else:
							HarmDataSourcesTitles.objects.create(title=title).save()
							title_obj = HarmDataSourcesTitles.objects.get(title=title)
						# print("General Title:{}, Source Title:{}, URL:{}, Model:{}".format(title, source, source_dict['url'], model))
						print("General Title:{}, Source Title:{}, URL:{}".format(title, source, source_dict['url']))
						temp = HarmDataSourcesLinks.objects.create(
													model=model_id, variable=variable_id,
													title=title_obj,
													var_source_info=source,
													var_source_url=source_dict['url'])
						temp.save()


