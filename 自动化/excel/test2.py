import requests
import lxml
import sys
from bs4 import BeautifulSoup
import xlwt
import time
import urllib
import xlwings as xw
import random


class tianyanspider():
    def __init__(self, start_row, end_row, filepath, txtpath):
        self.start_row = start_row
        self.end_row = end_row
        self.filepath = filepath
        self.txtpath = txtpath
        self.useragents = [
            'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'User-Agent:Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'User-Agent: MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'User-Agent, Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        ]
    # 获取代理池
    def get_proxypool(self):
        proxypool = []
        with open(self.txtpath, 'r') as f:
            for line in f.readlines():
                line1 = line.replace('\n', '')
                proxypool.append(line1)

        print(proxypool)
        return proxypool

    def get_useragent(self):
        l = len(self.useragents)
        i = random.randint(0,l-1)
        user_agent = self.useragents[i]

        return user_agent

    #验证代理池ip是否可用
    def verify_ip(self,proxypool):
        url = 'https://icanhazip.com/'
        

        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': '__cfduid=de9efa2a6f9fae06c541b573175a219b81568089958',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

        useful_proxypool = []
        for i in proxypool:
            ipaddr = i
            proxies = {'https': ipaddr}
            try:
                response = requests.get(url, proxies=proxies, timeout=1, headers=headers)
                if response.status_code == 200:
                    useful_proxypool.append(ipaddr)
                    print('success: ',ipaddr)
                    continue
                else:
                    print(response.status_code)
                    continue
            except requests.exceptions.ProxyError:
                print('代理服务器无法连接')
                continue
            except requests.exceptions.ConnectTimeout:
                print('useless ip address: ',ipaddr)
                continue
            except requests.exceptions.ReadTimeout:
                print('requests.exceptions.ReadTimeout: ',ipaddr)
                time.sleep(1)

        print(useful_proxypool)
        return useful_proxypool

    # 获取Excel中待爬取税号
    def get_tax_nums(self):
        start_row = int(self.start_row)
        end_row = int(self.end_row)

        tax_nums = []
        app = xw.App(add_book=False)
        wb = app.books.open(self.filepath)
        sheet1 = wb.sheets[0]

        for row in range(start_row, end_row):
            row_str = str(row)
            tax_num = sheet1.range('D'+row_str).value
            tax_nums.append(tax_num)

        wb.close()
        app.kill()
        print(tax_nums)
        return tax_nums

    # 获取信息
    def searchinf(self, tax_nums, proxypool):

        start_row=int(self.start_row)
        app=xw.App(add_book=False)
        wb=app.books.open(self.filepath)
        sheet2=wb.sheets[1]

        tax_nums = tax_nums
        proxypool = proxypool
        # user_agent = self.get_useragent()
        infolist = []

        headers = {
            'Host': 'm.tianyancha.com',
                    'Connection': 'keep-alive',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': self.get_useragent(),
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

            'Cookie': 'aliyungf_tc=AQAAALoIbTLUZAEAHk1CMeOl2r/QUQfs;csrfToken=Yrc2a9vwq3YVxktoG8TBGeRd;TYCID=a98e1260d2d811e98d5b2f26bc208dac;undefined=a98e1260d2d811e98d5b2f26bc208dac;Hm_lvt_d5ceb643638c8ee5fbf79d207b00f07e=1568016362;Hm_lpvt_d5ceb643638c8ee5fbf79d207b00f07e=1568016395;_ga=GA1.2.1825680567.1568016363; _gid=GA1.2.856838551.1568016363;ssuid=2708731936',
            'Host': 'm.tianyancha.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.get_useragent(),
        }

        lenp = len(proxypool)
        lent = len(tax_nums)
        p = 0
        t = 0

        while p < lenp and t < lent:
            url='https://m.tianyancha.com/search?key='+str(tax_nums[t])
            proxies={'https': proxypool[p]}
            try:
                response=requests.get(url, headers=headers1, proxies=proxies,timeout=5)
                soup=BeautifulSoup(response.text, 'lxml')
                code = response.status_code
                if code == 200:
                    soup=BeautifulSoup(response.text, 'lxml')
                    try:
                        info=soup.find('div', attrs={'class': 'search-name'})
                        compony_name=info.string
                        legal_name=soup.find('div', class_='title-val name-ellipsis').a['title']
                        url=info.a['href']

                    except AttributeError:
                        compony_name='没有找到相关企业'
                        legal_name=''
                        url=''
                        print('没有找到相关企业')
                    # info = (tax_nums[t], compony_name, legal_name, url)
                    print('爬取中',t)
                    # infolist.append(info)
                    row_str = str(start_row + t)
                    sheet2.range('A' + row_str).value = str(tax_nums[t])
                    sheet2.range('B' + row_str).value = compony_name
                    sheet2.range('C' + row_str).value = legal_name
                    sheet2.range('E' + row_str).value = url
                    t += 1
                elif code == 302:
                    print('被反爬了，换代理')
                    p += 1
                    continue
                else:
                    print(code)
                    p += 1
            except requests.exceptions.ProxyError:
                print('代理服务器无法连接，换')
                p += 1
            except requests.exceptions.ConnectTimeout:
                print('访问超时')
                p += 1
            # except:
            #     print('unknown error')
            #     continue

        if p == len(proxypool):
            print('ip用完了，爬到%d行' %(start_row+t))

        if t == len(tax_nums):
            print('num爬完了')
        
        print(f'爬了{t}个数据')
        wb.save()
        app.kill()
        # print(infolist)
        return infolist

    # 存入excel
    def save_to_excel(self, infolist):
        start_row=int(self.start_row)
        # end_row = int(self.end_row)
        app=xw.App(add_book=False)
        wb=app.books.open(self.filepath)
        sheet2=wb.sheets[1]
        num = len(infolist)
        i = 0
        while i < num:
            row_str = str(start_row+i)
            sheet2.range('A' + row_str).value = infolist[i][0]
            sheet2.range('B' + row_str).value = infolist[i][1]
            sheet2.range('C' + row_str).value = infolist[i][2]
            sheet2.range('E' + row_str).value = infolist[i][3]
            i += 1

            

        wb.save()
        wb.close()
        app.kill()



if __name__ == "__main__":
    start_row=1638
    end_row=1700
    filepath=r"E:\The-crawler-learn\自动化\副本单位信息.xlsx"
    txtpath=r'E:\The-crawler-learn\proxypool\66ip.txt'
    ty=tianyanspider(start_row, end_row, filepath, txtpath)
    
    tax_nums = ty.get_tax_nums()
    proxypool = ty.get_proxypool()

    useful_proxypool = ty.verify_ip(proxypool)

    infolist=ty.searchinf(tax_nums, useful_proxypool)


    # ty.save_to_excel(infolist)










#测试
    # start_row=1610
    # end_row=1700
    # filepath=r"E:\The-crawler-learn\自动化\副本单位信息.xlsx"
    # txtpath=r'E:\The-crawler-learn\proxypool\xici.txt'
    # ty=tianyanspider(start_row, end_row, filepath, txtpath)
    
    # tax_nums=['91320213727404559Q', '91320211758974917P']
    # useful_proxypool=['119.130.107.252:3128', '222.89.32.157:9999']
    # infolist=ty.searchinf(tax_nums, useful_proxypool)
    # infolist = [('91320213727404559Q', '无锡市永润电气有限公司', '张永源', 'https://m.tianyancha.com/company/2352229447'), ('91320211758974917P', '无锡宏亮化纤有限公司', '尤红良', 'https://m.tianyancha.com/company/704149814')]
    # if len(infolist) != 0:
    #     ty.save_to_excel(infolist)
    # else:
    #     print('未爬到数据')  
