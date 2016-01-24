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
     try:
         if x[0]=='(' and x[-1]==')':
            return -float(x[1:-2])
         else:
             return float(x)
     except: return None


def request(source_code, information):
    return  parse_table(
            find_section(source_code,information))


def get_annual_incomestatement_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock+'&annual'


def get_quarterly_incomestatement_url(stock):
    return 'https://finance.yahoo.com/q/is?s='+stock


def get_keystats_url(stock):
    return 'http://finance.yahoo.com/q/ks?s=' + stock


def get_source_code(url):
    return urllib2.urlopen(url).read()


def parse_table(source_code):
    source_code = source_code.split('</td></tr>')[0]
    source_code = source_code.replace('<strong>', '')
    source_code = source_code.replace('</strong>', '')
    source_code = source_code.replace('\n', '')
    source_code = source_code.replace('&nbsp;', '')
    source_code = source_code.replace('<td align="right">','')
    source_code = source_code.replace(' ', '')
    source_code = source_code.split('</td>')
    source_code = filter(None, source_code)
    return [float_or_none(x.replace(',', '')) for x in source_code]


def find_section(source_code, section_name):
    try:
        return source_code.split(section_name)[1]
    except:
        print 'failed acquiring ' + section_name