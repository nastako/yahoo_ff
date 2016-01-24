__author__ = 'Alexandre'

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

    def __init__(self, ticker):
        # assumes self is the ticker

        self.ticker = ticker

        self.incomestatement_annual_yahoo_html = get_source_code(
                                                 get_annual_incomestatement_url(self.ticker))

        self.__get_endofperiods()

        self.__get_totoalrevenue()
        self.__get_costofrevenue()
        self.__get_grossprofit()
        self.__get_sellinggeneralandadministrative()
        self.__get_nonrecurring()
        self.__get_otheroperatingexpenses()
        self.__get_totalotherincome()
        self.__get_ebit()
        self.__get_interestexpense()
        self.__get_incomebeforetax()
        self.__get_incometaxexpense()
        self.__get_minorityinterest()
        self.__get_netincomefromcontinuingops()
        self.__get_discontinuedoperations()
        self.__get_extraitems()
        self.__get_accountingchanges()
        self.__get_otheritems()
        self.__get_netincome()

        print 'Annual income statement for ' + str(self.ticker) + ' successfuly obtained'

    def get_annual_incomesatement(self):
        print   [self.endofperiods,
                 self.totalrevenue,
                 self.costofrevenue,
                 self.grossprofit,
                 self.sellinggeneralandadministrative,
                 self.nonrecurring,
                 self.otheroperatingexpenses,
                 self.totalotherincome,
                 self.ebit,
                 self.interestexpense,
                 self.incomebeforetax,
                 self.incometaxexpense,
                 self.minorityinterest,
                 self.netincomefromcontinuingops,
                 self.discontinuedoperations,
                 self.extraitems,
                 self.accountingchanges,
                 self.otheritems,
                 self.netincome]

    def __get_totoalrevenue(self):
        field = 'Total Revenue'
        self.totalrevenue = {field :
                annual_incomestatement_request(self.incomestatement_annual_yahoo_html, field)}

    def __get_costofrevenue(self):
        field = 'Cost of Revenue'
        self.costofrevenue = {field :
                annual_incomestatement_request(self.incomestatement_annual_yahoo_html, field)}

    def __get_grossprofit(self):
        field = 'Gross Profit'
        self.grossprofit = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_researchdevelopment(self):
        field = 'Research Development'
        return {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_sellinggeneralandadministrative(self):
        field = 'Selling General and Administrative'
        self.sellinggeneralandadministrative = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_nonrecurring(self):
        field = 'Non Recurring'
        self.nonrecurring = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_otheroperatingexpenses(self):
        field = 'Others'
        self.otheroperatingexpenses = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_totalotherincome(self):
        field = 'Total Other Income/Expenses Net'
        self.totalotherincome = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_ebit(self):
        field = 'Earnings Before Interest And Taxes'
        self.ebit = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_interestexpense(self):
        field = 'Interest Expense'
        self.interestexpense = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_incomebeforetax(self):
        field = 'Income Before Tax'
        self.incomebeforetax = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_incometaxexpense(self):
        field = 'Income Tax Expense'
        self.incometaxexpense = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_minorityinterest(self):
        field = 'Minority Interest'
        self.minorityinterest = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_netincomefromcontinuingops(self):
        field = 'Net Income From Continuing Ops'
        self.netincomefromcontinuingops = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_discontinuedoperations(self):
        field = 'Minority Interest'
        self.discontinuedoperations = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_extraitems(self):
        field = 'Extraordinary Items'
        self.extraitems = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_accountingchanges(self):
        field = 'Effect Of Accounting Changes'
        self.accountingchanges = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_otheritems(self):
        field = 'Other Items'
        self.otheritems = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}

    def __get_netincome(self):
        field = 'Net Income From Continuing Ops'
        self.netincome = {field : annual_incomestatement_request(self.incomestatement_annual_yahoo_html,
                field)}


    def __get_endofperiods(self):
        source_code = self.incomestatement_annual_yahoo_html
        end_periods = source_code.split('Period Ending')[1]
        end_periods = end_periods.split('</th></TR><tr>')[0]
        end_periods = end_periods.split('</th>')
        self.endofperiods = {'endofperiods' :[parser.parse(x[-12:]) for x in end_periods]}

