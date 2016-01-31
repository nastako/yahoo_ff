import time
from yahoo_ff import *
import pprint
import os
import pickle

def wait(seconds):
    time.sleep(seconds)


def main():
    pp = pprint.PrettyPrinter(indent=0)
    path = os.getcwd()

    #aapl = yahoo_ff('aapl')

    #pickle.dump(aapl, open('test.p', 'wb'))

    aapl = pickle.load(open('test.p', "rb"))

    pp.pprint (aapl.package_sec_annually().head())

    pp.pprint (aapl.pricehistory.resample('M').head())

if __name__ == "__main__":
    main()
