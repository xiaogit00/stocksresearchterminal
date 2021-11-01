import pandas as pd
import pandas_datareader.data as web
import datetime
import pandas_market_calendars as mcal
from pandas_datareader import wb

class Price:

    def __init__(self, ticker):
                        #Pulling Price info and getting Pct_change Column
        s_price = web.DataReader(ticker, 'yahoo', start='1960-1-1')['Adj Close']

        print('Stock Initialized')
        s_price_yearly = s_price.resample('BYS').first()
        s_pct_change = s_price_yearly.pct_change()
        mean = s_pct_change.mean()
        startYear = s_price.index[0].date().year
        s_std = s_price_yearly.std()
                        #Building both to DataFrame
        frame = {'price' : s_price_yearly, 'pct_change': s_pct_change}
        df = pd.DataFrame(frame)

                    #Generating historic mean
        self.mean = mean
        self.price = df['price']
        self.s_price_yearly = s_price_yearly
        self.pct_change = s_pct_change
        self.startYear = startYear
        self.std = s_std


    def hmean(self, startYear, endYear):
        s_price_period = self.s_price_yearly['{}'.format(startYear): '{}'.format(endYear)]
        mean = s_price_period.pct_change().mean()
        infln_df = wb.download(indicator='FP.CPI.TOTL.ZG', country='US', start=int(startYear), end=int(endYear))
        infln_df.index = infln_df.index.droplevel(0) #dropping multilevel index
        infln_df.columns = ['infln'] #changing column name
        infln_df = infln_df.sort_index()
        infln_df = infln_df['infln']/100
        infln_df.index = pd.to_datetime(infln_df.index).year
        s_returns_period = s_price_period.pct_change()
        s_returns_period.index = s_returns_period.index.year
        realAAR = (s_returns_period - infln_df).dropna().mean()
        return mean, realAAR

    def gmean(self, startYear, endYear):
        s_price_period = self.s_price_yearly['{}'.format(startYear): '{}'.format(endYear)]
        cumulativeReturns = (s_price_period.pct_change()+1).cumprod().tail(1)[0]
        yeardiff = int(endYear) - int(startYear)
        gmean = ((cumulativeReturns)**(1/yeardiff)-1)
        s_returns_period = self.pct_change['{}'.format(startYear): '{}'.format(endYear)]
        cv = s_returns_period.std()/gmean
        return gmean, cumulativeReturns, cv

    def stdev(self, startYear, endYear):
        s_returns_period = self.pct_change['{}'.format(startYear): '{}'.format(endYear)]
        sd = s_returns_period.std()
        return sd
