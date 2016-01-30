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

    # try:
    #     f = open('sp500.txt', 'r').read()
    #     split_file = f.split('\n')
    #     ticker = 'aapl'
    #
    #     for ticker in split_file:
    #         wait(.2)
    #         data = yahoo_ff('aapl')
    #         isa = pd.DataFrame(data.incomestatement_annual)
    #         bsa = pd.DataFrame(data.balancesheet_annual)
    #         csa = pd.DataFrame(data.cashflow_annual)
    #         df = pd.merge(isa,bsa,on='endofperiod')
    #         df1 = pd.merge(df,csa,on='endofperiod')
    #         df1.set_index('endofperiod', inplace=True)
    #         df1.transpose().to_csv(path + '/database/' + ticker + '_annual.csv')
    #         wait(.2)
    #         isa = pd.DataFrame(data.incomestatement_quarterly)
    #         bsa = pd.DataFrame(data.balancesheet_quarterly)
    #         csa = pd.DataFrame(data.cashflow_quarterly)
    #         df = pd.merge(isa, bsa, on='endofperiod')
    #         df1 = pd.merge(df, csa, on='endofperiod')
    #         df1.set_index('endofperiod', inplace=True)
    #         df1.transpose().to_csv(path + '/database/' + ticker + '_quarterly.csv')
    #
    # except Exception,e:
    #     print 'failed in mainloop at ' + ticker + ' ' + str(e)


if __name__ == "__main__":
    main()
