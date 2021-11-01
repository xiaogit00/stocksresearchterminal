# Stocks Research Terminal
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759165/Screenshot_2021-11-01_at_5.32.25_PM_dse5m2.png)
### This is a command line based stocks research terminal that'll enable you to find:

✅ Historic price for stock since start of IPO  
✅ The Average Annualized Returns between a specified period  
✅ The cumulative returns (geometric mean) between a specified period  
✅ Risk (standard deviation) of a stock  
✅ Inflation adjusted average annualized returns  

All in one click!



### Installation  & Usage
1. Install the following dependencies from pip / brew:  
`pip install pandas`  
`pip install pandas-datareader`  
`pip install datetime`  
`pip install pandas_market_calendars`  
Also, make sure python is intalled.

2. Clone the project folder into your computer

3. cd to project folder

4. Simply run:
`python3 s.py`

5. Follow the terminal instructions to get what you need!

Examples:  
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759873/Screenshot_2021-11-01_at_5.44.30_PM_dciq3e.png)
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759815/Screenshot_2021-11-01_at_5.42.41_PM_lpdyh5.png)
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759804/Screenshot_2021-11-01_at_5.43.16_PM_hdijgo.png)
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759730/Screenshot_2021-11-01_at_5.42.02_PM_evv5x2.png)


### Additional Pricing Charts:
![](https://res.cloudinary.com/dl4murstw/image/upload/v1635759515/Screenshot_2021-11-01_at_5.38.27_PM_sv9qqq.png)
If you want a chart like this above, install the following:
`pip install pandas`  
`pip install sys`  
`pip install matplotlib`   
1. In current project directory, simply run `python3 pricePlot.py <ticker> <yearStart>` to get a graph of the historic price of your stock from the yearStart to date!
e.g. `python3 pricePlot.py GOOGL 2005`
