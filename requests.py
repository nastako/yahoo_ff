author = 'Alexandre'

from dateutil import parser
from tools import *


#TODO get_metadata

#TODO get_keystats

def get_mc(stock):
    source_code = get_source_code(get_keystats_url(stock))
    mc = source_code.split(
         'Market Cap (intraday)<font '
         'size="-1"><sup>5</sup></font>:</td><td '
         'class="yfnc_tabledata1"><span id="yfs_j10_')[-1].split(
         '</span>')[0].split('>')[-1]
    return float_or_none(parse_powers(mc))


def get_prm(stock):
    source_code = get_source_code(get_keystats_url(stock))
    prm = source_code.split(
         'Profit Margin (ttm):</td><td class="yfnc_tabledata1">')[-1].split(
         '%</td>')[0]
    return float_or_none(prm)


def get_roa(stock):
    source_code = get_source_code(get_keystats_url(stock))
    roa = source_code.split(
        'Return on Assets (ttm):</td><td class="yfnc_tabledata1">'
        )[-1].split('%</td>')[0]
    return float_or_none(roa)


class yahoo_ff:
    incomestatement_fields = ['Total Revenue',
                              'Cost of Revenue',
                              'Gross Profit',
                              'Research Development',
                              'Selling General and Administrative',
                              'Non Recurring',
                              'Total Operating Expenses',
                              'Total Other Income/Expenses Net',
                              'Earnings Before Interest And Taxes',
                              'Interest Expense',
                              'Income Before Tax',
                              'Income Tax Expense',
                              'Minority Interest',
                              'Net Income From Continuing Ops',
                              'Discontinued Operations',
                              'Extraordinary Items',
                              'Effect Of Accounting Changes',
                              'Other Items',
                              'Net Income Applicable To Common Shares']

    def __init__(self, ticker):
        self.ticker = ticker
        self.__construct_incomestatement_annual()
        self.__construct_incomestatement_quarterly()


    def __construct_incomestatement_annual(self):
        html = get_source_code(get_annual_incomestatement_url(self.ticker))
        self.incomestatement_annual = self.__get_endofperiods(html)
        for field in self.incomestatement_fields:
            self.incomestatement_annual[field] = request(html, field)

        print 'Annual income statement for ' + str(self.ticker) + ' successfuly obtained'

    def __construct_incomestatement_quarterly(self):
        html = get_source_code(get_quarterly_incomestatement_url(self.ticker))
        self.incomestatement_quarterly = self.__get_endofperiods(html)
        for field in self.incomestatement_fields:
            self.incomestatement_quarterly[field] = request(html, field)

        print 'Quarterly income statement for ' + str(self.ticker) + ' successfuly obtained'

    def __get_endofperiods(self, html):
        source_code = html
        end_periods = source_code.split('Period Ending')[1]
        end_periods = end_periods.split('</th></TR><tr>')[0]
        end_periods = end_periods.split('</th>')
        return {'endofperiods': [parser.parse(x[-12:]) for x in end_periods]}






