from yahoo_ff import *
import os

# TODO create_database
# TODO update_database


class database:
    '''class contains incomestatement, balancesheet, cashflow and price history for a ticker'''
    formatlist = '.txt'

    def __init__(self, list):
        self.name = list
        self.filename = list + database.formatlist
        self.location = os.getcwd() + '/' + list + '_db/'

        # create the database with for loop, make pickle file for each

        # sp500.take('aapl') loads pickle and returns yahoo_ff object
