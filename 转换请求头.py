import re
import pprint


str = '''
Host:	api9.tianyancha.com
Content-Type:	application/json
Accept-Encoding:	br, gzip, deflate
Connection:	keep-alive
Accept:	*/*
version:	TYC-XCX-WX
User-Agent:	Mozilla/5.0 (iPad; CPU OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.5(0x17000523) NetType/WIFI Language/zh_CN
Authorization:	0###oo34J0beoAhM0IoWyOLzirF1kQXg###1568356205540###2ea40530930146ed6bf6672dea1cad77
Referer:	https://servicewechat.com/wx9f2867fc22873452/27/page-frame.html
Accept-Language:	zh-cn
'''

pattern = re.compile(r'(.*):\s(.*)')

result = re.findall(pattern,str)

headers = {

}
for i in result:
    headers[i[0]] = i[1]

pprint.pprint(headers)
