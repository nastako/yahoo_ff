__author__ = 'Alexandre'

import urllib2
from dateutil import parser



def parse_powers(x):
    powers = {'B': 10 ** 9, 'M': 10 ** 6, 'T': 10 ** 12}
    try:
        power = x[-1]
        return float(x[:-1]) * powers[power]
    except TypeError:
        return x


def float_or_none(x):
     try: return float(x)
     except: return None


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


def get_source_code(url):
    return urllib2.urlopen(url).read()


def get_income_statement_a_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock+'&annual'


def get_income_statement_q_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock


def get_keystats_url(stock):
    return 'http://finance.yahoo.com/q/ks?s=' + stock


def yahoo_key_stats(stock):
    try:
        pass
    except Exception, e:
        print 'failed in the main loop ', str(e)


def get_revenues_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    revenues = source_code.split('Total Revenue')[1]
    revenues = revenues.split('</td></tr><tr>')[0]
    revenues = revenues.replace(' ','')
    revenues = revenues.replace('<strong>', '')
    revenues = revenues.replace('</strong>','')
    revenues = revenues.replace('\n','')
    revenues = revenues.replace('</td><tdalign="right">','')
    revenues = revenues.split('&nbsp;')[:-1]
    revenues = filter(None,revenues)
    return [float(x.replace(',','')) for x in revenues]


def get_grossprofit_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    grossprofit = source_code.split('Gross Profit')[1]
    grossprofit = grossprofit.split('</td></tr><tr>')[0]
    grossprofit = grossprofit.replace(' ','')
    grossprofit = grossprofit.replace('<strong>', '')
    grossprofit = grossprofit.replace('</strong>','')
    grossprofit = grossprofit.replace('\n','')
    grossprofit = grossprofit.replace('</td><tdalign="right">','')
    grossprofit = grossprofit.split('&nbsp;')[:-1]
    grossprofit = filter(None, grossprofit)
    return [float(x.replace(',','')) for x in grossprofit]


def get_researchdevelopment_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    researchdevelopment = source_code.split('Research Development')[1]
    researchdevelopment = researchdevelopment.split('</td></tr><tr>')[0]
    researchdevelopment = researchdevelopment.replace(' ','')
    researchdevelopment = researchdevelopment.replace('<strong>', '')
    researchdevelopment = researchdevelopment.replace('</strong>','')
    researchdevelopment = researchdevelopment.replace('\n','')
    researchdevelopment = researchdevelopment.replace('</td><tdalign="right">','')
    researchdevelopment = researchdevelopment.split('&nbsp;')[:-1]
    researchdevelopment = filter(None, researchdevelopment)
    return [float(x.replace(',','')) for x in researchdevelopment]

def get_nonrecurring_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    researchdevelopment = source_code.split('Non Recurring')[1]
    researchdevelopment = researchdevelopment.split('</td></tr><tr>')[0]
    researchdevelopment = researchdevelopment.replace(' ','')
    researchdevelopment = researchdevelopment.replace('<strong>', '')
    researchdevelopment = researchdevelopment.replace('</strong>','')
    researchdevelopment = researchdevelopment.replace('\n','')
    researchdevelopment = researchdevelopment.replace('</td><tdalign="right">','')
    researchdevelopment = researchdevelopment.split('&nbsp;')[:-1]
    researchdevelopment = filter(None, researchdevelopment)
    return [float_or_none(x.replace(',','')) for x in researchdevelopment]


def get_endperiods_a(stock):
    source_code = get_source_code(get_income_statement_a_url(stock))
    end_periods = source_code.split('Period Ending')[1]
    end_periods = end_periods.split('</th></TR><tr>')[0]
    end_periods = end_periods.split('</th>')
    return [parser.parse(x[-12:]) for x in end_periods]
