import mitmproxy
from mitmproxy import ctx

class aWei():
    def request(self,flow:mitmproxy.http.HTTPFlow):
        if flow.request.host != 'www.baidu.com':
            return
    
        ctx.log.info('有人在用百度搜索：%s' % flow.request.query.get('wd'))
        flow.request.query.set_all('wd',['c语言'])
    
    def response(self,flow:mitmproxy.http.HTTPFlow):
        text = flow.response.get_text()
        text = text.replace('c语言','python')
        flow.response.set_text(text)


addons = [
    aWei()
]