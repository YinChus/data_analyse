# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    #定义书名属性
    title = scrapy.Field()
    #定义作者属性
    author = scrapy.Field()
    #定义推荐度属性
    recommen = scrapy.Field()
    #定义价格属性
    price = scrapy.Field()

#实例化一个dangdangItem对象
book = DangdangItem()
book['title'] = '云边有个小卖部'
book['author'] = '张嘉佳'
book['recommen'] = '100%'
book['price'] = '21.00'
print(book,'\n',type(book))