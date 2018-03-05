import pandas as pd
import numpy as np



class Data_Handler():
    def __init__(self):
        self.hi = "Hi"
        self._table = pd.read_csv('Alcohol_Data/alcohol_data.csv')
    
    def get_wine(self):
        for index, item in self._table.iterrows():
            yield item