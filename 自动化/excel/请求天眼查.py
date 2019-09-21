#-*- coding-8 -*-
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwings as xw
import time
import urllib
import json

def open_excel():
    app = xw.App(add_book=False)
    wb = app.books.open(filepath)
    sheet1 = wb.sheets[0]
    sheet2 = wb.sheets[1]

    sheets = (sheet1,sheet2)
    return sheets

def get_tax_num(row,sheet1):
    row = str(row)
    tax_num = sheet1.range('D'+row).value
    return tax_num

def search(tax_num):
    headers = {
'Accept': '*/*',
 'Accept-Encoding': 'br, gzip, deflate',
 'Accept-Language': 'zh-cn',
 'Authorization': '0###oo34J0beoAhM0IoWyOLzirF1kQXg###1568356205540###2ea40530930146ed6bf6672dea1cad77',
 'Connection': 'keep-alive',
 'Content-Type': 'application/json',
 'Host': 'api9.tianyancha.com',
 'Referer': 'https://servicewechat.com/wx9f2867fc22873452/27/page-frame.html',
 'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN',
 'version': 'TYC-XCX-WX'
    }
    url = f'https://api9.tianyancha.com/services/v3/search/sNorV4/{tax_num}?pageSize=10&sortType=0&pageNum=1'
    proxies = {'https':'203.6.149.130:80'}
    response = requests.get(url,headers=headers,verify=True,proxies=proxies)
    if response.status_code == 200:
        dic = {}
        data = response.text
        json_data = json.loads(data)
        try:
            compony_name = json_data['data']["companyList"][0]["name"]
            legal_name = json_data['data']["companyList"][0]["legalPersonName"]
            phone = json_data['data']["companyList"][0]["phoneNum"]
            businessScope = json_data['data']["companyList"][0]["businessScope"]
            regCapital = json_data['data']["companyList"][0]["regCapital"]
            regLocation = json_data['data']["companyList"][0]["regLocation"]
            dic['compony_name'] = compony_name
            dic['legal_name'] = legal_name
            dic['phone'] = phone
            dic['businessScope'] = businessScope
            dic['regCapital'] = regCapital
            dic['regLocation'] = regLocation
            return dic
        except IndexError:
            return ''
        
    else:
        print(response.status_code)
        return ''

def write_to_excel(row_str,dic,sheet2):
    row_str = str(row_str)
    sheet2.range('A' + row_str).value = str(tax_num)
    sheet2.range('B' + row_str).value = dic['compony_name']
    sheet2.range('C' + row_str).value = dic['legal_name']
    sheet2.range('D' + row_str).value = dic['phone']
    sheet2.range('E' + row_str).value = dic['businessScope']
    sheet2.range('F' + row_str).value = dic['regCapital']
    sheet2.range('G' + row_str).value = dic['regLocation']



if __name__ == "__main__":
    start_row=1750  
    end_row=2300
    filepath=r"E:\The-crawler-learn\自动化\副本单位信息.xlsx"
    app = xw.App(add_book=False)
    wb = app.books.open(filepath)
    sheet1 = wb.sheets[0]
    sheet2 = wb.sheets[1]
    for row in range(start_row, end_row):
        tax_num = get_tax_num(row,sheet1)
        print(tax_num)
        dic = search(tax_num)
        if dic != '':
            write_to_excel(row,dic,sheet2)
            time.sleep(1)
        else:
            continue

    print('success')