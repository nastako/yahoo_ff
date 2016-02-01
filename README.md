# yahoo_ff
package to obtain financial fundamental data for stocks

## Requirements
```
pip install Quandl
```

```
pip install pandas
```

```
pip install pickle
```

## Steps
```
aapl = yahoo_ff('aapl')
```

*aapl* will be an object from which the following DataFrames can be extracted:

for price history, volume and other...
```
aapl.pricehistory
```
for balancesheet, incomestatement, cashflow all in the same DataFrame:
```
aapl.package_sec_annually
```