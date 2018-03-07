import pandas as pd
import numpy as np
import csv
#import LiquorView


class Data_Handler():
    def __init__(self):
        # Wine is the best preview
        self._wine = pd.read_csv('Alcohol_Data/wine.csv')
        
        # Get other files for init
        self._beer = pd.read_csv('Alcohol_Data/beer_spirits.csv')
        self._spirits = pd.read_csv('Alcohol_Data/beer_spirits.csv')
        self._liqour = pd.read_csv('Alcohol_Data/liquor_coolers_ciders_data_sake.csv')
        self._coolers = pd.read_csv('Alcohol_Data/liquor_coolers_ciders_data_sake.csv')
        self._sake= pd.read_csv('Alcohol_Data/liquor_coolers_ciders_data_sake.csv')
        self._cider= pd.read_csv('Alcohol_Data/liquor_coolers_ciders_data_sake.csv')

    # Return all beers in new variable
    # self._temp['Category'] gives you beers/spirits need a way ti filter out spirits
    # More efficient to sort if called upon.
    def get_beer(self):
        self._beer = (self._beer.loc[self._beer["Category"] == "BEER"])
        for index, item in self._beer.iterrows():
            yield item

    def get_spirits(self):
        self._spirits = (self._spirits.loc[self._spirits["Category"] == "SPIRITS"])
        for index, item in self._spirits.iterrows():
            yield item
            
    def get_coolers(self):
        self._coolers = (self._coolers.loc[self._coolers["Category"] == "COOLER"])
        for index, item in self._coolers.iterrows():
            yield item

    def get_cider(self):
        self._cider = (self._cider.loc[self._cider["Category"] == "CIDER"])
        for index, item in self._cider.iterrows():
            yield item

    # Can format here instead of other place it was used at.
    # It will print faster and suggested.
    def get_wine(self):
        for index, item in self._wine.iterrows():
            yield item

    # Doesn't have correct csv format, no data output
    # Liqueur is labled Spirit -- Liqour or other -- Liqour
    def get_liqour(self):
        self._liqour = (self._liqour.loc[self._liqour["Category"] == "LIQUEUR"])
        for index, item in self._liqour.iterrows():
            yield item
    # Sake is labled Spirit -- Sake or other -- Sake
    def get_sake(self):
        self._sake = (self._sake.loc[self._sake["Category"] == "SAKE"])
        for index, item in self._sake.iterrows():
            yield item
