__author__ = 'Alexandre'

import urllib2


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



def yahoo_income_statement_request(stock, information):
    return  parse_table(
            find_section(
            get_source_code(
            get_income_statement_a_url(stock)),information))


def get_income_statement_a_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock+'&annual'


def get_income_statement_q_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock


def get_keystats_url(stock):
    return 'http://finance.yahoo.com/q/ks?s=' + stock


def get_source_code(url):
    return urllib2.urlopen(url).read()


def parse_table(source_code):
    source_code = source_code.split('</td></tr><tr>')[0]
    source_code = source_code.replace(' ', '')
    source_code = source_code.replace('<strong>', '')
    source_code = source_code.replace('</strong>', '')
    source_code = source_code.replace('\n', '')
    source_code = source_code.replace('</td><tdalign="right">', '')
    source_code = source_code.split('&nbsp;')[:-1]
    source_code = filter(None, source_code)
    return [float_or_none(x.replace(',', '')) for x in source_code]



def find_section(source_code, section_name):
    return source_code.split(section_name)[1]