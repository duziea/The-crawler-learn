from aip import AipOcr

config = {
    'appId':'17016769',
    'apiKey':'knaMhoomtcEueKYSaGLluloG',
    'secretKey':'2DXkVdlC46iUvLVi6oE2ijTjyfaSfGAA'
}

client = AipOcr(**config)

def get_file_content(filepath):
    with open(filepath,'rb') as fp:
        return fp.read()
    
image = get_file_content('./image/test5.png')

result = client.basicGeneral(image)
# result = client.basicGeneralUrl('https://mmbiz.qpic.cn/mmbiz_png/J2icnQspGlaIBasoawV1Qb9jxicia9lmmvnNZlskhyppWN1lZfzMCoDN8jTsslUZicCxHx1G03SvgZwotQm50Ha05w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1')
print(result)
for i in result.get('words_result'):
    print(i.get('words'))
    