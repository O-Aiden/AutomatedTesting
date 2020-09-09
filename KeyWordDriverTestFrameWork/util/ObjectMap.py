"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : ObjectMap.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time


def get_element(driver, by, locator):
    """查找单一元素"""
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return element


def get_elements(driver, by, locator):
    """获取一组元素"""
    try:
        elements = WebDriverWait(driver, 10).until(lambda x: x.find_element(by, locator))
    except Exception as e:
        raise e
    else:
        return elements


if __name__ == "__main__":
    d = webdriver.Chrome()
    d.get('https://mail.126.com')
    time.sleep(5)
    iframe = d.find_element_by_tag_name('iframe')
    # d.switch_to.frame(get_element(d, 'xpath', "KeyWordDriverTestFrameWork-master"))
    d.switch_to.frame(iframe)
    #loc = (By.CSS_SELECTOR,'#auto-id-1597843513342')
    #username = get_element(d, 'CSS_SELECTOR','#auto-id-1597843513342')
    #username.send_keys('linuxxiaochao')
    d.find_element_by_name('email').send_keys('123')
    d.find_element_by_name('password').send_keys('456')
    time.sleep(3)
    d.switch_to.default_content()
    d.quit()
