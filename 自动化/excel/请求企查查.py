#-*- coding-8 -*-
import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib

key_word = '91320281MA1PBCEN1E'

re = 'https://www.tianyancha.com/search?key='+key_word

headers = {
            'Host': 'www.tianyancha.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': re,#'https://www.tianyancha.com/search?key=%E5%B1%B1%E4%B8%9C%20%E7%A7%91%E6%8A%80',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': r'ssuid=2767685789; TYCID=0dcfc510b12411e9838cbdd23c764dc3; undefined=0dcfc510b12411e9838cbdd23c764dc3; _ga=GA1.2.1401633399.1564310404; aliyungf_tc=AQAAAJNjv1WilQIAwUxCMb/6KrDgvHCZ; csrfToken=_d82O3kT0QJGjRfFhv-niO3I; _gid=GA1.2.54004409.1566628168; RTYCID=492597e9598349dfafe0fe5454348ce2; CT_TYCID=64702c4dcbe2430ea083219b808f9cfe; bannerFlag=true; jsid=SEM-BAIDU-PP-VI-000873; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E5%2591%25A8%25E7%2591%259C%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%25224%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc1MTUwMDIyOSIsImlhdCI6MTU2NjYzMTM3NiwiZXhwIjoxNTk4MTY3Mzc2fQ.D8AcMUt0KWDkzPCXRl-uCIgPwnsLNjqmflYDnffpVkPeI793DcKZoS0py0foSBZI8RV47qeBqHQmWPBw4SbXUA%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217751500229%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc1MTUwMDIyOSIsImlhdCI6MTU2NjYzMTM3NiwiZXhwIjoxNTk4MTY3Mzc2fQ.D8AcMUt0KWDkzPCXRl-uCIgPwnsLNjqmflYDnffpVkPeI793DcKZoS0py0foSBZI8RV47qeBqHQmWPBw4SbXUA; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1566635673,1566636118,1566636401,1566636434; cloud_token=b4e588b63ded42d9af31598457df7c6d; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1566637898',
            }

response = requests.get(re,headers = headers)

soup = BeautifulSoup(response.text,'lxml')

# com_all_info = soup.body.select('#web-content > div > div.container-left > div.search-block.header-block-container > div.result-list.sv-search-container > div > div > div.content > div.header > a')

compony_name = soup.find('a',attrs={'class':'name'}).string
legal_name = soup.find('a',attrs={'class':'legalPersonName link-click'}).string
contact = soup.find('div',attrs={'class':'contact row'})
phone = soup.select('#web-content > div > div.container-left > div.search-block.header-block-container > div.result-list.sv-search-container > div > div > div.content > div.contact.row > div:nth-child(1) > span:nth-child(2) > span')[0].string

contact = contact.get_text()
print(contact)
print(compony_name)
print(legal_name)
print(phone)


