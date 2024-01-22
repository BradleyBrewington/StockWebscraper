from autoscraper import AutoScraper

url = 'https://www.quiverquant.com/stock/ROAD/'


wanted_list = ['Purchase', 'Sale']

scraper = AutoScraper()
print(scraper.build(url, wanted_list))




scraper.save('GetTradeType')


#returns a list of purchase and sale, the first item is the most recent
