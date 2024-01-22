from autoscraper import AutoScraper

url = 'https://www.quiverquant.com/stock/ROAD/'


scraper = AutoScraper()

scraper.load('nameScraper')
data = scraper.get_result(url, grouped=True)
print(data)