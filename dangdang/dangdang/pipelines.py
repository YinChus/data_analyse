# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl 

class DangdangPipeline(object):
    def __init__(self):
        self.wb=openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.title = '2020图书销售榜单'
        self.ws.append(['图书名称','作者','推荐度','价格'])
        #设置列宽，方便查看表格数据
        self.ws.column_dimensions['A'].width = 55
        self.ws.column_dimensions['B'].width = 40
        self.ws.column_dimensions['C'].width = 13

    def process_item(self, item, spider):
        line = [item['title'],item['author'],item['recommen'],item['price']]
        self.ws.append(line)
        return item
    def close_spider(self,spider):
        self.wb.save('..\\爬取结果.xlsx')
        self.wb.close()