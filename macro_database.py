from yahoo_ff import yahoo_ff
import os
import Quandl
import pickle
from keys import quandl
# TODO check if exists already, check if all files are there

class macro_database:
    '''creates a pickle database for several macro economic components'''

    def __init__(self, option):
        if option == 'spy':
            self.__create_spy()

    def __create_spy(self):
        df = Quandl.get('YAHOO/INDEX_GSPC', tirm_start='1980-01-01')
        df['Adjusted Close'] = (df['Adjusted Close'] - df['Adjusted Close'][0])/df['Adjusted Close'][0]*100
        df.resample('M')
        df.rename(columns = {'Adjusted Close':'sp500'}, inplace = True)
        df = df['sp500']
        return df


    def take(self, data):
        # return the yahoo_ff object that was stored in a pickle file of the database
        return pickle.load(open(self.location + data + '.p', 'rb'))
