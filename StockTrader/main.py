from autoscraper import AutoScraper
import robin_stocks.robinhood as r
import time
import random

username = input("Username: ")
password = input("Password: ")
login = r.login(username, password, store_session=True) #login to robinhood



scraper = AutoScraper()             #loads the Quiver Quantitative senate name scraper





def getStockName(url):                               
   """
   WORKS --> Runs NameScraper and returns string of stock names
    returns a list of all the unique stock names  
   """
   scraper.load('nameScraper') 
   return scraper.get_result(url, unique=True)




def stocksToPurchase():  
    """
    WORKS --> inserts the name of each stock into the URL to get its
    respective info page, pulls a list of the most recent 
    transactions (runs getTradeType) has to wait 6 seconds between
    each stock to avoid getting blocked by website, returns 
    list of stocks recently bought
    
    converts to a list, gets rid of stocks that were sold, gets rid of things that arent stocks, returns a list to buy
    """
    stockList = list(getStockName('https://www.quiverquant.com/sources/senatetrading'))[0]
    scraper.load('GetTradeType')
    #print(stockList)
    print("Analyzing: https://www.quiverquant.com/sources/senatetrading\nPlease be patient...")
    for i in stockList[:]:
        #print(i+': ')
        
        time.sleep(6)
        #print(scraper.get_result('https://www.quiverquant.com/stock/'+i+'/'))
        typeOfTrade = list(scraper.get_result('https://www.quiverquant.com/stock/'+i+'/'))
        #print(typeOfTrade)
        if typeOfTrade == [[],[]] or typeOfTrade[0][0] != 'Purchase':
           stockList.remove(i)


    
    return stockList



def presentData():
    cash = float(r.load_account_profile().get('buying_power')) #load cash in account
    wishlist = stocksToPurchase()
    numStocksToBuy = len(wishlist)
    print()
    print(f"Buying Power: {cash}")

    text = f"""
Analyzed all the recent trades posted on: https://www.quiverquant.com/sources/senatetrading
Of those trades, {numStocksToBuy} of them have been purchased recently:

"""
    print(text)
    for i in wishlist[:]:
       # r.order_buy_fractional_by_price(i, 1)
        print(i)

    wantToBuy = input("Would you like to purchase these stocks? (y/n)")

    print(wantToBuy)

    if(wantToBuy=="y" or wantToBuy=="Y" or wantToBuy=="yes" or wantToBuy=="YES" or wantToBuy=="Yes" or wantToBuy=="1"):
        buyStocks(wishlist)
    else:
        print("Have a good day")
    return 0


def buyStocks(wishlist):  
    """
    Takes a dollar amount as input, buys that amount of each stock
    """
    fractionalAmount = float(input("Enter dollar amount per stock to purchase: "))


    for i in wishlist[:]:
        r.order_buy_fractional_by_price(i, fractionalAmount)
        print(f"Submitted order for {i}")
        time.sleep(6)
    
    return 0





presentData()


