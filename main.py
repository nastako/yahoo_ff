import pprint
from stocks_database import stocks_database
import pandas as pd
from yahoo_ff import *


def main():
    pp = pprint.PrettyPrinter(indent=0)

    sp500test = stocks_database('sp500test')



if __name__ == "__main__":
    main()
