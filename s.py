from price import Price

newTicker = 'yes'

while newTicker == 'yes':
    ticker = input("""
    *****************************************************
    *****************************************************
    Type the ticker you want to research:""")

    print('Initializing stock...')

    stock = Price(ticker)
    prompt = """


    """
    selection = int(input("""
    Select what you want to know:
    1. Historic mean
    2. AAR between periods
    3. Price for years
    4. Geometric Mean
    5. Std Deviation (Risk)
    6. Inflation adjusted AAR
    """))
    newTicker = 'no'
    while selection != 0 and newTicker == 'no':
        if selection == 1:
            print('\n')
            print("Historic mean since {}: {:.1%}".format(stock.startYear, round(stock.mean,2)))
            selection = int(input('\nPlease select what else you want OR \nPress 0 to exit program, 9 to select new ticker.  '))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
        elif selection == 2 :
            print('\n')
            startYear = input('Start year? ')
            endYear = input('End year?')
            print("\nAAR between {} and {}: {:.1%}\n".format(startYear, endYear, round(stock.hmean(startYear, endYear)[0],2)))
            print("Calculating real AAR...")
            print("Inflation Adjusted AAR: {:.1%}".format(round(stock.hmean(startYear, endYear)[1],2)))
            selection = int(input('Please select what else you want OR \nPress 0 to exit program, 9 to select new ticker. '))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
        elif selection == 3:
            print('\n')
            print(stock.price)
            selection = int(input("""Please select what else you want.
            1. Historic mean
            2. AAR between periods
            3. Price for years
            Press 0 to exit program OR \n9 to select new ticker. """))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
        elif selection == 4 :
            print('\n')
            startYear = input('Start year? ')
            endYear = input('End year?')
            print("\nGeometric mean between {} and {}: {:.1%}\n".format(startYear, endYear, round(stock.gmean(startYear, endYear)[0],2)))
            print("\nCumulative returns over same period is: {}".format(round(stock.gmean(startYear, endYear)[1],2)))
            selection = int(input('Please select what else you want OR \nPress 0 to exit program, 9 to select new ticker. '))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
        elif selection == 5:
            print('\n')
            startYear = input('Start year? ')
            endYear = input('End year?')
            print("\nStandard Deviation between {} and {}: {:.1%}.\n CV = {}".format(startYear, endYear, round(stock.stdev(startYear, endYear),2), round(stock.gmean(startYear, endYear)[2], 2)))
            print("Initializing Std Deviation of S&P500 between similar period...")
            sp500 = Price('^gspc')
            print("\nStd Deviation of S&P500 between similar period is {:.1%}\nCV = {}\n".format(round(sp500.stdev(startYear, endYear), 2), round(sp500.gmean(startYear, endYear)[2], 2)))
            selection = int(input('Please select what else you want OR \nPress 0 to exit program, 9 to select new ticker. '))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
        else:
            selection = int(input('Please select what you want OR \nPress 0 to exit program, 9 to select new ticker. '))
            if selection == 9:
                newTicker = 'yes'
            else:
                newTicker = 'no'
