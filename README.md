# yahoo_ff
Package to obtain financial fundamental data as well as price history for stocks. Creates 
database to be quickly used later.

## Installation
```
pip install yahoo_ff
```

## Using

### A single stock
```
aapl = yahoo_ff('aapl')
```
will create an object from which several Pandas DataFrames of interst can be extracted
```
aapl.incomestatement_annual
aapl.incomestatement_quarterly
aapl.balancesheet_annual
aapl.balancesheet_quarterly
aapl.cashflow_annual
aapl.cashflow_quarterly
aapl.pricehistory
```
Note: *pricehistory* includes Open, High, Low, Close, Volume, Ex-Divident, Split Ratio, Adj.Open,
 Adj.High, Adj.Low, Ajd.Close, Adj.Volume.
 
To simplify a bit further,
```
aapl.package_sec_annually()
```
will return all annual data from the three SEC filings (incomestatement, balancesheet, cashflow) 
in one single DataFrame.

### Create a database for a list of stocks  
You can use it later quickly, or get it updated. If you have a list of stocks such as a file dbtest
.csv
```
dbtest = stocks_database('dbtest')
```
will create a folder named *dbtest_db* in the root directory with all the data stored as a pickle
file. The object *dbtest* will now be available for you to access stocks stored in the database 
using the *take('aapl')* function as follows:
```
dbtest.take('aapl').pricehistory
```
and all other data as described in section above.
Note: *take('aapl')* returns None if stock does not exist in the database object.

## Next updates:
- Create an automatic updating flow of a database.