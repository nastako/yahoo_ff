from yahoo_ff import yahoo_ff
import os
import pickle


# TODO check if exists already, check if all files are there

class stocks_database:
    '''creates a pickle database for a list of tickers specified in list.format file'''
    format = '.csv'

    def __init__(self, list):

        self.name = list
        self.filename = list + stocks_database.format # which file do you read to construct it
        self.location = os.getcwd() + '/' + list + '_db/'
        if not os.path.exists(self.location):
            os.makedirs(self.location)
            self.__create()
        else:
            print 'database ' + self.name + ' already exists'

    def __create(self):
        # create the database with for loop, make pickle file for each
        with open(self.filename, 'r') as f:
            tickers = (f.read().split())
            for ticker in tickers:
                pickle.dump(yahoo_ff(ticker), open(self.location + ticker + '.p', 'wb'))
                print 'added ' + ticker + ' to database ' + self.name

    def take(self, ticker):
        # return the yahoo_ff object that was stored in a pickle file of the database
        return pickle.load(open(self.location + ticker + '.p', 'rb'))
