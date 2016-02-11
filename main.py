import pprint

from yahoo_ff.stocks_database import stocks_database


def main():
    pp = pprint.PrettyPrinter(indent=0)

    dbtest = stocks_database('dbtest')

    pp.pprint(dbtest.take('aapl').pricehistory.head())
    empty_space()
    pp.pprint(dbtest.take('aapl').package_sec_annually().head())
    empty_space()
    pp.pprint(dbtest.take('aapl').package_sec_quarterly().head())
    empty_space()


    pp.pprint(dbtest.take('tsla').pricehistory.head())
    empty_space()
    pp.pprint(dbtest.take('tsla').package_sec_annually().head())
    empty_space()
    pp.pprint(dbtest.take('tsla').package_sec_quarterly().head())
    empty_space()


    pp.pprint(dbtest.take('ibm').pricehistory.head())
    empty_space()
    pp.pprint(dbtest.take('ibm').package_sec_annually().head())
    empty_space()
    pp.pprint(dbtest.take('ibm').package_sec_quarterly().head())
    empty_space()


def empty_space():
    print '\n'


if __name__ == "__main__":
    main()
