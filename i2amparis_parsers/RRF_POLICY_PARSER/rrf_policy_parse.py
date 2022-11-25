import xlrd
from pprint import pprint as pp
from i2amparis_main.models import *

class Parser:
    def __init__(self, f):
        self.f = f
        self.book = xlrd.open_workbook(f)
        model_titles_france ={ 
                                0:'pillar', 
                                1:'axis',
                                2:'rff_type',
                                3:'title', 
                                5:'description',
                                6:'budget',
                                7:'total_ratio',
                                11:'first_classification',
                                12:'second_classification'
                                }

        model_titles ={ 
                                0:'pillar', 
                                1:'axis',
                                2:'rff_type',
                                3:'title', 
                                5:'description',
                                6:'budget',
                                7:'total_ratio',
                                10:'first_classification',
                               11:'second_classification'
               }
        self.end_col = {
                            'Greece': 168,
                            'Belgium': 143,
                            'France': 84,
                            'Germany': 42,
                            'Italy': 182,
                            'Spain':215
                        }
        cols_france = [0,1,2,3,5,6,7,11,12]
        cols = [0,1,2,3,5,6,7,10,11]
        for c in list(self.end_col.keys()):
            if c == 'France':
                self.read_excel(c,self.end_col[c] , cols_france, model_titles_france)
            else:
                self.read_excel(c,self.end_col[c] , cols, model_titles)
            self.parse_db()

    def read_excel(self,country,end_col, lst_idxs, model_fields):
        s = self.book.sheet_by_name(country)
        self.data = []
        for i in range(1, end_col):
            temp_dict = {}
            temp_row= s.row_values(i)
            temp_col = {}
            for c,v in enumerate(temp_row):
                if c in lst_idxs:
                    temp_col[model_fields[c]] = v
            temp_col['country'] = country
            temp_col['total_ratio'] = round(temp_col['total_ratio'],2)
            self.data.append(temp_col)

    def parse_db(self):
        for i in self.data:
            pp(i)
            t=RrfPolicy(**i)
            t.save()
                 
        



