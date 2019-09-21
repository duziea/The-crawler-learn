from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
import base64

def b_login(username,password):
    driver = webdriver.Chrome()
    driver.get('https://passport.bilibili.com/login')

    username_input = driver.find_element_by_css_selector('#login-username')
    username_input.send_keys(username)
    password_input = driver.find_element_by_css_selector('#login-passwd')
    password_input.send_keys(password)
    denglu = driver.find_element_by_css_selector('#geetest-wrap > ul > li.btn-box > a.btn.btn-login')
    denglu.click()


    JS = 'return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png");'
    im_info = driver.execute_script(JS)
    im_base64 = im_info.split(',')[1]  #拿到base64编码的图片信息
    im_bytes = base64.b64decode(im_base64)  #转为bytes类型
    with open('bg.png','wb') as f:  #保存图片到本地
        f.write(img_data)
if __name__ == "__main__":
    username = 'rw1040230003@163.com'
    password = 'renwei123'
    b_login(username,password)