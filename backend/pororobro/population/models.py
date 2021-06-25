from django.db import models
import pandas as pd
import numpy as np
from pororobro.common.models import Reader , Printer, FileDTO


class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()
        self.population = None

    def organize_population_data(self):
        f = self.f
        r = self.r
        p = self.p
        pop = self.population
        f.context = './data/'
        f.fname = '05. population_raw_data'
        pop = r.xls(f)
        pop.fillna(method='pad', inplace=True)
        pop.rename(columns={'행정구역(동읍면)별(1)': '광역시도',
                                   '행정구역(동읍면)별(2)': '시도',
                                   '계': '인구수'}, inplace=True)

        pop = pop[(pop['시도'] != '소계')]

        print(pop)












