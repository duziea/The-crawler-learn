import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib
import xlwings as xw


#获取代理池
def get_proxypool(name):
    proxypool = []
    with open(r'E:\The-crawler-learn\proxypool\\' + name + '.txt', 'r') as f:
        for line in f.readlines():
            line1 = line.replace('\n', '')
            proxypool.append(line1)

    print(proxypool)
    return proxypool

def get_tax_nums(start_row,end_row,filepath):
    start_row = int(start_row)
    end_row = int(end_row)

    tax_nums = []
    app = xw.App(add_book=False)
    wb = app.books.open(filepath)
    sheet1 = wb.sheets[0]
  
    for row in range(start_row,end_row):
        row_str = str(row)
        tax_num = sheet1.range('D'+row_str).value
        tax_nums.append(tax_num)

    wb.close()
    app.kill()
    print(tax_nums)
    return tax_nums

def searchinf(tax_nums,proxypool):
    dic = {}
    headers = {
                'Host': 'm.tianyancha.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Sec-Fetch-Site': 'none',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'Cookie': r'ssuid=2767685789; TYCID=0dcfc510b12411e9838cbdd23c764dc3; undefined=0dcfc510b12411e9838cbdd23c764dc3; _ga=GA1.2.1401633399.1564310404; aliyungf_tc=AQAAAJNjv1WilQIAwUxCMb/6KrDgvHCZ; csrfToken=_d82O3kT0QJGjRfFhv-niO3I; bannerFlag=true; jsid=SEM-BAIDU-PP-VI-000873; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2591%25A8%25E7%2591%259C%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25224%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc1MTUwMDIyOSIsImlhdCI6MTU2NjYzMTM3NiwiZXhwIjoxNTk4MTY3Mzc2fQ.D8AcMUt0KWDkzPCXRl-uCIgPwnsLNjqmflYDnffpVkPeI793DcKZoS0py0foSBZI8RV47qeBqHQmWPBw4SbXUA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217751500229%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc1MTUwMDIyOSIsImlhdCI6MTU2NjYzMTM3NiwiZXhwIjoxNTk4MTY3Mzc2fQ.D8AcMUt0KWDkzPCXRl-uCIgPwnsLNjqmflYDnffpVkPeI793DcKZoS0py0foSBZI8RV47qeBqHQmWPBw4SbXUA; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1566635673,1566636118,1566636401,1566636434; cloud_token=b4e588b63ded42d9af31598457df7c6d; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1566873485; _gid=GA1.2.862619327.1566873485; _gat_gtag_UA_123487620_1=1',
                }
    headers1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'aliyungf_tc=AQAAALoIbTLUZAEAHk1CMeOl2r/QUQfs;csrfToken=Yrc2a9vwq3YVxktoG8TBGeRd;TYCID=a98e1260d2d811e98d5b2f26bc208dac;undefined=a98e1260d2d811e98d5b2f26bc208dac;Hm_lvt_d5ceb643638c8ee5fbf79d207b00f07e=1568016362;Hm_lpvt_d5ceb643638c8ee5fbf79d207b00f07e=1568016395;_ga=GA1.2.1825680567.1568016363; _gid=GA1.2.856838551.1568016363;ssuid=2708731936',
        'Host': 'm.tianyancha.com',
        'Referer': 'https://m.tianyancha.com/search?key=31320000466293984D',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    }
    
    proxypool = proxypool
    lenp = len(proxypool)
    lent = len(tax_nums)
    p = 0
    t = 0

    while p <= lenp and t <= lent:
        url = 'https://m.tianyancha.com/search?key='+str(tax_nums[t])
        proxies = {'https':proxypool[p]}
        try:
            response = requests.get(url,headers = headers1,proxies= proxies)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text,'lxml')
                try:
                    info = soup.find('div',attrs={'class':'search-name'})
                    dic['compony_name'] = info.string
                except AttributeError:
                    dic['compony_name'] = '没有找到相关企业'
                    print('没有找到相关企业')
                if dic['compony_name'] == '没有找到相关企业':
                    return None
                else:
                    dic['legal_name'] =soup.find('div',class_='title-val name-ellipsis').a['title']
                    dic['url'] = info.a['href']

            elif response.status_code == 302:
                print('被反爬了，换ip')
                p +=1
                continue
        except:
            print('unknown error')
            continue

        if p == len(proxypool):
            print('ip用完了')
            break

        if n == len(tax_nums):
            print('num爬完了')
            break
    
    return dic

# def save_to_excel(start_row,end_row,filepath):
    app = xw.App(add_book=False)
    wb = app.books.open(filepath)
    sheet2 = wb.sheets[1]
    if dic == None:
        continue
    else:
        sheet2.range('A' + row_str).value = tax_num
        sheet2.range('B' + row_str).value = dic['compony_name']
        sheet2.range('C' + row_str).value = dic['legal_name']
#         # sheet2.range('D' + row_str).value = dic['phone']
        sheet2.range('E' + row_str).value = dic['url']



if __name__ == "__main__":
    get_proxypool('66ip')