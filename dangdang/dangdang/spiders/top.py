import scrapy
import bs4
from ..items import DangdangItemS

class dangdangSpaider(scrapy.Spider):
    name = 'dangdang'
    allow_domains = ['bang.dangdang.com']
    start_urls = []
    for i in range(1,3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2021-0-1-' + str(i)
        start_urls.append(url)
    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        books = soup.find('ul',class_='bang_list clearfix bang_list_mode').find_all('li')
        for book in books:
            item = DangdangItem()
            item['title'] = book.find('div',class_ = 'name').find('a')['title']
            item['author'] = book.find('div',class_='publisher_info').text
            item['recommen'] = book.find('div',class_='star').find('span',class_='tuijian').text
            item['price'] = book.find('div',class_='price').find('span',class_='price_n').text
            print(item['title'],item['author'],item['recommen'],item['price'])
            yield item 

