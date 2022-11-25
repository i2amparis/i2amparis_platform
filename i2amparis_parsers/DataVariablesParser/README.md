# How use data parser

First download Django project [i2amparis](https://gitlab.epu.ntua.gr/paris-reinforce/i2amparis).\
Inside **i2amparis** clone the project [Parsers](https://gitlab.epu.ntua.gr/paris-reinforce/i2amparis_parsers).\
Now open shell of project,

```sh 
python3 manage.py shell
```

Inside shell we call the function,

```python
from i2amparis_parsers.DataVariablesParser import export_json as ej
ej.export_json(<file path>,<boolean parse in db or not>,<sheet index>,<name of model where we want to parse data>)
# For example 
ej.export_json(path=f) # If we want to parse data in table ResultsComp and read sheet with index zero
# Otherwise
ej.export_json(path=f, parse=False, sheet=1) # We want to check sheet with index 1(second sheet in excel) and we don't want to parse data in our db
# Another case
ej.export_json(path=f, sheet=2, table_name='WWHEUResultsComp') # Read sheet with index two and parse data in table WWHEUResultsComp 

```


**NOTE**
1. The given file, excel must have the format as is given in [simple_file.xlsx](https://gitlab.epu.ntua.gr/paris-reinforce/i2amparis_parsers/-/blob/master/DataVariablesParser/sample_file.xlsx)
2. The given models must have same name as we,already, stored in our database, in model **DataVariablesModels**
3. If you want you can check the excel file without parsed in db, in that case parameter **parse** must be *False*
4. In case we doesn't define the *table_name* the data will parse in table *ResultsComp*

For more info check the comments in [export_json.py](https://gitlab.epu.ntua.gr/paris-reinforce/i2amparis_parsers/-/blob/master/DataVariablesParser/export_json.py)

