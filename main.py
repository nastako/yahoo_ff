import pprint
from stocks_database import stocks_database



def main():
    pp = pprint.PrettyPrinter(indent=0)

    sp500test = stocks_database('sp500')


if __name__ == "__main__":
    main()
