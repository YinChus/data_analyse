from bs4 import BeautifulSoup as bs
import requests
from fake_useragent import UserAgent
import pandas as pd
import openpyxl as pxl
ua = UserAgent()#请求伪装，利用fake-useragent包
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
           'Accept': 'application/json, text/plain, */*',
           'Accept-Encoding':'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cookie':'_ga=GA1.2.1867791142.1664246050; _gid=GA1.2.580705938.1665133438; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1664246039,1665133437,1665212177; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1665215052; kw_token=H44A574KGJI',
           'csrf': 'H44A574KGJI',
           'Host': 'www.kuwo.cn',
           'Connection': 'keep-alive',
           'Refer':'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%B7%B1'}

url_com='http://www.kuwo.cn/comment'
url_lic='http://m.kuwo.cn/newh5/singles/songinfoandlrc'
url1="http://www.kuwo.cn/play_detail/186749128"


lic_par={
    'musicId': '151848190', 
    'httpsStatus': '1',
    'reqId': '037f9980-3e3b-11ed-9ee9-cdab120ffbba'
    }
res_lic=requests.get(url1,headers=headers)
lic=res_lic.json()

lic_list=lic["data"]["lrclist"]
for lic in lic_list:
    lyric=lic["lineLyric"]
    print(lyric,"\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
wb=pxl.Workbook()
mysheet=wb.active
mysheet.title="songs"
mysheet["A1"]="music_com"
'''
for i in range(3):
    com_parrams={
        
        'type': 'get_comment',
        'f': 'web',
        'page': str(i+1),
        'rows': '60',
        'digest': '15',
        'sid': '151848190',
        'uid': '0',
        'prod': 'newWeb',
        'httpsStatus': '1',
        'reqId': '3de62610-3e37-11ed-a027-4964ac4ccc4b'
        }
    res_com=requests.get(url_com,params=com_parrams,headers=headers)
    new_com=res_com.json()
    count=0
    new_com_list=new_com["rows"]
    for com in new_com_list:
        com_text=com["msg"]
        music_com=com["msg"]
        mysheet.append([music_com])
        print(com_text,"\n")
        count+=1
    
wb.save("songs_com.xlsx")  
print(count)
'''









