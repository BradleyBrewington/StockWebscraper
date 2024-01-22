from autoscraper import AutoScraper

url = 'https://www.quiverquant.com/sources/senatetrading'


wanted_list = ['PSQ']

scraper = AutoScraper()
scraper.build(url, wanted_list)



data = scraper.get_result(url, grouped=True)

print(data)


scraper.save('nameScraper')


#pulls from Quiverguant