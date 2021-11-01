#python3 price.py BABA 2015 
import pandas as pd
import datetime
import sys
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style

##Write a function that takes the following inputs (stock ticker name, start year), and returns
# the chart as output


def hPrice(ticker, startYear):

    start = datetime.datetime(startYear,1,1)
    end = datetime.datetime.now()

    df = web.DataReader(ticker, 'yahoo',start, end)
    mpl.rc('figure', figsize=(7,6))
    style.use('ggplot')

    df['Adj Close'].plot(label= ticker)
    plt.legend()
    plt.title('Price of {}'.format(ticker))
    plt.show(block=True)


hPrice(sys.argv[1], int(sys.argv[2]))
