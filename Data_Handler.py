import pandas as pd
import numpy as np
import csv
from Widgets.Search_Widgets.LiquorViewItem import LiquorViewItem


class Data_Handler():
    def __init__(self):
        # Wine is the best preview
        self._wine = pd.read_csv('Alcohol_Data/wine.csv')
        
        # Get other files for init
        self._beer = pd.read_csv('Alcohol_Data/beer.csv')
        self._spirits = pd.read_csv('Alcohol_Data/spirits.csv')
        self._liqour = pd.read_csv('Alcohol_Data/liquer.csv')
        self._coolers = pd.read_csv('Alcohol_Data/cooler.csv')
        self._sake= pd.read_csv('Alcohol_Data/sake.csv')
        self._cider= pd.read_csv('Alcohol_Data/cider.csv')


    def search_bar(self, string, non_char, number):
        print('SEARCHING...')
        temp_df = pd.read_csv('Alcohol_Data/{}.csv'.format(string.lower()))
        abv = temp_df['Alcohol_By_Volume'].tolist()
        #self._all_data = (self._all_data.loc[self._all_data['Category'] == string])
        searched_data = pd.read_csv('Alcohol_Data/searched.csv')
        print('Checking Fromatting...')
        #with open(('Alcohol_Data/searched.csv'.format(string.lower())), 'a') as file:
            
        #y = pd.read_csv('Alcohol_Data/{}.csv'.format(string.lower()))

        print('Checking Non-Character Values...')
        for i in range(len(temp_df)):
            if non_char == '<':
                # temp_num = str(abv[i])
                # temp_df = temp_df.loc[temp_df['Alcohol_By_volume'] == temp_num]
                #self._searched_data = self._all_data.loc[lambda searched_data: searched_data.Alcohol_By_Volume < int(number), :]
                pass
            else:
                # x = str(self._beer.loc[lambda searched_data: searched_data.Alcohol_By_Volume > int(number), :])
                pass
            
        print('List Succesfull')
        print('Initializing Loop.')
        for index, item in temp_df.iterrows():
            yield self.make_object(item, "search_result")

        print("COMPLETE!")
        
    # made a comment
    # Return all beers in new variable
    # self._temp['Category'] gives you beers/spirits need a way ti filter out spirits
    # More efficient to sort if called upon.
    def get_beer(self):
        self._beer = (self._beer.loc[self._beer["Category"] == "BEER"])
        for index, item in self._beer.iterrows():
            yield self.make_object(item, "search_result")

    def get_spirits(self):
        self._spirits = (self._spirits.loc[self._spirits["Category"] == "SPIRITS"])
        for index, item in self._spirits.iterrows():
            yield self.make_object(item, "search_result")
            
    def get_coolers(self):
        self._coolers = (self._coolers.loc[self._coolers["Category"] == "COOLER"])
        for index, item in self._coolers.iterrows():
            yield self.make_object(item, "search_result")

    def get_cider(self):
        self._cider = (self._cider.loc[self._cider["Category"] == "CIDER"])
        for index, item in self._cider.iterrows():
            yield self.make_object(item, "search_result")

    # Can format here instead of other place it was used at.
    # It will print faster and suggested.
    def get_wine(self):
        for index, item in self._wine.iterrows():
            yield self.make_object(item, "search_result")

    # Doesn't have correct csv format, no data output
    # Liqueur is labled Spirit -- Liqour or other -- Liqour
    def get_liqour(self):
        self._liqour = (self._liqour.loc[self._liqour["Category"] == "WINE -- LIQUEUR"])
        for index, item in self._liqour.iterrows():
            yield self.make_object(item, "search_result")

    # Sake is labled Spirit -- Sake or other -- Sake
    def get_sake(self):
        self._sake = (self._sake.loc[self._sake["Category"] == "WINE -- SAKE"])
        for index, item in self._sake.iterrows():
            yield self.make_object(item, "search_result")

    def get_cabinet(self):
        self._cabinet = pd.read_csv('Alcohol_Data/cabinet.csv')
        for index, item in self._cabinet.iterrows():
            yield self.make_object(item, "cabinet")
        
    def make_object(self, entry, entry_type: str):
        additional_fields = []
        if entry_type == "search_result":
            additional_fields = ["sub_category"]
        elif entry_type == "cabinet":
            additional_fields = ["sub_category", "quantity"]

        item = LiquorViewItem(entry['ID'],
                                        entry['Name'].replace('\'', ''),
                                        entry['Maker'],
                                        entry['Category'], 
                                        entry['Sub_Category'], 
                                        entry['Sub_Sub_Category'],
                                        entry['Sub_Sub_Sub_Category'],
                                        float(entry['Cost']),
                                        float(entry['Volume(ml)']),
                                        float(entry['Alcohol_By_Volume']),
                                        entry['Aroma'],
                                        entry['Color'],
                                        entry['Origin'],
                                        entry['Region'])
        item.setText(0, item.get_name().title())
        column_index = 1

        if "maker" in additional_fields:
            item.setText(column_index, item.get_maker().title())
            column_index += 1
        if "category" in additional_fields:
            item.setText(column_index, item.get_category().title())
            column_index += 1
        if "sub_category" in additional_fields:
            try:
                item.setText(column_index, item.get_sub_category().title())
                column_index += 1
            except:
                print("something went wrong")
        if "sub_sub_category" in additional_fields:
            item.setText(column_index, item.get_sub_sub_category().title())
            column_index += 1
        if "sub_sub_sub_category" in additional_fields:
            item.setText(column_index, item.get_sub_sub_sub_category().title())
            column_index += 1
        if "quantity" in additional_fields:
            item.setText(column_index, str(entry["Quantity"]))
            column_index += 1

        return item
