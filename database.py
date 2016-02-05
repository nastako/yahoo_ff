from yahoo_ff import yahoo_ff
import os
import pickle
import time

# TODO check if exists already, check if all files are there

class database:
    '''creates a pickle database for a list of tickers specified in list.format file'''
    format = '.txt'

    def __init__(self, list):
        self.name = list
        self.filename = list + database.format # which file do you read to construct it
        self.location = os.getcwd() + '/' + list + '_db/'
        if not os.path.exists(self.location):
            os.makedirs(self.location)
            self.__create()

    def __create(self):
        # create the database with for loop, make pickle file for each
        with open(self.filename, 'rb') as list:
            for ticker in list:
                try:
                    pickle.dump(yahoo_ff(ticker), open(self.location + ticker + '.p', 'wb'))
                    print 'added ' + ticker + ' to database ' + self.name
                    self.wait(0.2)
                except:
                    print 'failed getting data for ' + ticker

    def __wait(seconds):
        time.sleep(seconds)

    def take(self, ticker):
        # return the yahoo_ff object that was stored in a pickle file of the database
        return pickle.load(open(self.location + ticker + '.p', 'rb'))
