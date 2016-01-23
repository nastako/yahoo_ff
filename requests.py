__author__ = 'Alexandre'

from dateutil import parser
from tools import *


#TODO def get_metadata(stock)


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


def get_totoalrevenue_a(stock):
    return yahoo_income_statement_request(stock, 'Total Revenue')


def get_costofrevenue_a(stock):
    return yahoo_income_statement_request(stock, 'Cost of Revenue')


def get_grossprofit_a(stock):
    return yahoo_income_statement_request(stock, 'Gross Profit')


def get_researchdevelopment_a(stock):
    return yahoo_income_statement_request(stock, 'Research Development')


def get_nonrecurring_a(stock):
    return yahoo_income_statement_request(stock, 'Non Recurring')


def get_endperiods_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    end_periods = source_code.split('Period Ending')[1]
    end_periods = end_periods.split('</th></TR><tr>')[0]
    end_periods = end_periods.split('</th>')
    return [parser.parse(x[-12:]) for x in end_periods]

