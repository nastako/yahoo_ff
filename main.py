import pprint
from database import database



def main():
    pp = pprint.PrettyPrinter(indent=0)

    sp500test = database('sp500test')

    pp.pprint (sp500test.take('tsla').package_sec_annually().head())

    pp.pprint (sp500test.take('tsla').pricehistory.resample('M').head())

if __name__ == "__main__":
    main()
