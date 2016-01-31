__author__ = 'Alexandre'

import time
from yahoo_ff import *
import pprint
import os


def wait(seconds):
    time.sleep(seconds)


def main():
    pp = pprint.PrettyPrinter(indent=0)
    path = os.getcwd()

    data = yahoo_ff('aapl')
    data.package_sec_annually().to_csv('aapl.csv')

if __name__ == "__main__":
    main()
