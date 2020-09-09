"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : KeyBoardUtil.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from selenium import webdriver

"""windows"""
# import win32api
# import win32con
# from selenium import webdriver
#
#
# class KeyBoardKeys(object):
#     """模拟键盘"""
#     # 键盘编码
#     vk_code = {
#         'enter': 0x0D,
#         'tab': 0x09,
#         'ctrl': 0x11,
#         'v': 0x56
#     }
#
#     @staticmethod
#     def key_down(key_name):
#         """模拟按下键"""
#         try:
#             win32api.keybd_event(KeyBoardKeys.vk_code[key_name], 0, 0, 0)
#         except Exception as e:
#             raise e
#
#     @staticmethod
#     def key_up(key_name):
#         """释放键"""
#         try:
#             win32api.keybd_event(KeyBoardKeys.vk_code[key_name], 0, win32con.KEYEVENTF_KEYUP, 0)
#         except Exception as e:
#             raise e
#
#     @staticmethod
#     def one_key(key):
#         """模拟单个按键"""
#         try:
#             KeyBoardKeys.key_down(key)
#             KeyBoardKeys.key_up(key)
#         except Exception as e:
#             raise e
#
#     @staticmethod
#     def two_keys(key1, key2):
#         """模拟组合按键"""
#         try:
#             KeyBoardKeys.key_down(key1)
#             KeyBoardKeys.key_down(key2)
#             KeyBoardKeys.key_up(key1)
#             KeyBoardKeys.key_up(key2)
#         except Exception as e:
#             raise e
"""mac"""

#encoding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
ActionChains1 = ActionChains(driver)
class KeyBoardKeys(object):
    @staticmethod
    def twoKeys(key1):
        """

        模拟组合键
        :param key1:Keys.CONTROL
        :param key2:'a'
        :return:
        """
        ActionChains(driver).key_down(key1).key_up(key1).perform()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('python')
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(3)
    k =KeyBoardKeys
    k.twoKeys(Keys.ENTER)
    time.sleep(3)
    #KeyBoardKeys.one_key('enter')
