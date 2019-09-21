from aip import AipOcr
import re
APP_ID='17016769'
API_KEY ='knaMhoomtcEueKYSaGLluloG'
SECRECT_KEY='2DXkVdlC46iUvLVi6oE2ijTjyfaSfGAA'
client=AipOcr(APP_ID,API_KEY,SECRECT_KEY)
i=open('./image/test1.png','rb')
img=i.read()
message=client.basicGeneral(img)
print(message)