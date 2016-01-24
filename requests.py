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

    balancesheet_fields =    ['Cash And Cash Equivalents',
                              'Short Term Investments',
                              'Net Receivables',
                              'Inventory',
                              'Other Current Assets',
                              'Total Current Assets',
                              'Long Term Investments',
                              'Property Plant and Equipment',
                              'Goodwill',
                              'Intangible Assets',
                              'Accumulated Amortization',
                              'Other Assets',
                              'Deferred Long Term Asset Charges',
                              'Total Assets',
                              'Accounts Payable',
                              'Short/Current Long Term Debt',
                              'Other Current Liabilities',
                              'Total Current Liabilities',
                              'Long Term Debt',
                              'Other Liabilities',
                              'Deferred Long Term Liability Charges',
                              'Minority Interest',
                              'Negative Goodwill',
                              'Total Liabilities',
                              'Misc Stocks Options Warrants',
                              'Redeemable Preferred Stock',
                              'Preferred Stock',
                              'Common Stock',
                              'Retained Earnings',
                              'Treasury Stock',
                              'Capital Surplus',
                              'Other Stockholder Equity',
                              'Total Stockholder Equity',
                              'Net Tangible Assets']

    def __init__(self, ticker):
        self.ticker = ticker
        self.__construct_incomestatement_annual()
        self.__construct_incomestatement_quarterly()
        self.__construct_balancesheet_annual()
        self.__construct_balancesheet_quarterly()

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

    def __construct_balancesheet_annual(self):
        html = get_source_code(get_annual_balancesheet_url(self.ticker))
        self.balancesheet_annual = self.__get_endofperiods(html)
        for field in self.balancesheet_fields:
            self.balancesheet_annual[field] = request(html, field)

        print 'Annual balance sheet for ' + str(self.ticker) + ' successfuly obtained'

    def __construct_balancesheet_quarterly(self):
        html = get_source_code(get_quarterly_balancesheet_url(self.ticker))
        self.balancesheet_quarterly = self.__get_endofperiods(html)
        for field in self.balancesheet_fields:
            self.balancesheet_quarterly[field] = request(html, field)

        print 'Quarterly balance sheet for ' + str(self.ticker) + ' successfuly obtained'

    def __get_endofperiods(self, html):
        source_code = html
        end_periods = source_code.split('Period Ending')[1]
        end_periods = end_periods.split('</TR>')[0]
        end_periods = end_periods.replace('<TD class="yfnc_modtitle1" align="right"><b>','')
        end_periods = end_periods.replace('<th scope="col" style="border-top:2px solid '
                                          '#000;text-align:right; font-weight:bold">','')
        end_periods = end_periods.replace('</span></small></td>','')
        end_periods = end_periods.replace('</span></small></TD>','')
        end_periods = end_periods.replace('</b>','')

        end_periods = end_periods.split('</th>')
        if len(end_periods) == 1:
            end_periods = end_periods[0].split('</TD>')

        return {'endofperiods': [parser.parse(x[-12:]) for x in end_periods if x is not '']}






