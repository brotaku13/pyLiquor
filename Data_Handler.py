import pandas as pd
import numpy as np
import csv
import re
from Widgets.Search_Widgets.LiquorViewItem import LiquorViewItem


class Data_Handler():
    """Qt5 implements an MV design structure, not MVC. The various app widgets in our project all assist with the View portion of MV
    Data_Handler is the only object that touches and interacts with the data we have in our CSV files. it is responsible for filtering, 
    searching, and feeding information to the widgets throughout the app. 

    Implemented as a singleton
    """


    def __init__(self):
        # Wine is the best preview
        self._wine = pd.read_csv('Alcohol_Data/wine.csv')
        self._beer = pd.read_csv('Alcohol_Data/beer.csv')
        self._spirits = pd.read_csv('Alcohol_Data/spirits.csv')
        self._liqour = pd.read_csv('Alcohol_Data/liquer.csv')
        self._coolers = pd.read_csv('Alcohol_Data/cooler.csv')
        self._sake= pd.read_csv('Alcohol_Data/sake.csv')
        self._cider= pd.read_csv('Alcohol_Data/cider.csv')
        self._all = pd.read_csv('Alcohol_Data/all_data.csv')
        
    def search(self, search_args: str):
        """Performs the filtering of the data necessary for a search. returns 
        only results matching the criteria provided by the search_args
        
        Arguments:
            search_args {str} -- The arguments given by the user
        """

        pattern = r'{}'.format(search_args.upper())
        results = self._all[self._all.Name.str.contains(pattern) | 
                            self._all.Maker.str.contains(pattern) | 
                            self._all.Category.str.contains(pattern) | 
                            self._all.Sub_Category.str.contains(pattern) |
                            self._all.Origin.str.contains(pattern) | 
                            self._all.Region.str.contains(pattern)]
        for index, item in results.iterrows():
            yield self.make_object(item, "search_result")

    def formatted_search(self, search_args: str):
        """Allows the user to perform a formatted search
        
        Arguments:
            search_args {str} -- Search Argument
        """
        args = search_args.split(' ')
        results = self._all
        op = args[1]
        l_value = args[0]
        try:
            if l_value == 'abv':
                if op == '>':
                    results = results[results.Alcohol_By_Volume > float(args[2])]
                elif op == '<':
                    results = results[results.Alcohol_By_Volume < float(args[2])]
                elif op == '=':
                    results = results[results.Alcohol_By_Volume == float(args[2])]
            else:
                if op == '=':
                    results = results[results[args[0].title()] == args[2].upper()]
        except Exception as e:
            print(str(e))
        
        for index, item in results.iterrows():
            yield self.make_object(item, "search_result")
        

    def get_beer(self):
        """Returns all beer entries
        """

        self._beer = (self._beer.loc[self._beer["Category"] == "BEER"])
        for index, item in self._beer.iterrows():
            yield self.make_object(item, "search_result")

    def get_spirits(self):
        """returns all spirits entries
        """

        self._spirits = (self._spirits.loc[self._spirits["Category"] == "SPIRITS"])
        for index, item in self._spirits.iterrows():
            yield self.make_object(item, "search_result")
            
    def get_coolers(self):
        """returns all coolers entries
        """

        self._coolers = (self._coolers.loc[self._coolers["Category"] == "COOLER"])
        for index, item in self._coolers.iterrows():
            yield self.make_object(item, "search_result")

    def get_cider(self):
        """returns all cider entries
        """

        self._cider = (self._cider.loc[self._cider["Category"] == "CIDER"])
        for index, item in self._cider.iterrows():
            yield self.make_object(item, "search_result")

    def get_wine(self):
        """returns all wine entries
        """

        for index, item in self._wine.iterrows():
            yield self.make_object(item, "search_result")

    # Doesn't have correct csv format, no data output
    # Liqueur is labled Spirit -- Liqour or other -- Liqour
    def get_liqour(self):
        """returns all Liqeur entries
        """

        self._liqour = (self._liqour.loc[self._liqour["Category"] == "WINE -- LIQUEUR"])
        for index, item in self._liqour.iterrows():
            yield self.make_object(item, "search_result")

    # Sake is labled Spirit -- Sake or other -- Sake
    def get_sake(self):
        """returns all sake entries
        """

        self._sake = (self._sake.loc[self._sake["Category"] == "WINE -- SAKE"])
        for index, item in self._sake.iterrows():
            yield self.make_object(item, "search_result")

    def get_cabinet(self):
        """returns all cabinet entries
        """

        self._cabinet = pd.read_csv('Alcohol_Data/cabinet.csv')
        for index, item in self._cabinet.iterrows():
            yield self.make_object(item, "cabinet")
        
    def make_object(self, entry, entry_type: str):
        """Factory method for creating LiquorViewItem objects
        
        Arguments:
            entry {Pandas.Series} -- A row from a pandas dataframe
            entry_type {str} -- defines which text columns to fill
        
        Returns:
            [type] -- [description]
        """

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
