"""
------------------------------------
@Time : 2019/8/3 14:20
@Auth : linux超
@File : ClipboardUtil.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
import subprocess
from selenium import webdriver


class Clipboard(object):

    @staticmethod
    def get_text():
        """获取剪切板的内容"""
        try:
            p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
            retcode = p.wait()
            data = p.stdout.read()
            # 这里的data为bytes类型，之后需要转成utf-8操作


        except Exception as e:
            raise e
        else:
            return data

    @staticmethod
    def set_text(value):
        """设置剪切板内容"""
        try:
            value = bytes(value, 'utf8')
            p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
            p.stdin.write(value)
            p.stdin.close()
            p.communicate()
        except Exception as e:
            raise e


if __name__ == '__main__':
    data = 'python'
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    query = driver.find_element_by_id('kw')
    Clipboard.set_text(data)
    clValue = Clipboard.get_text()
    query.send_keys(clValue.decode('utf-8'))
