"""
------------------------------------
@Auth : Yuki
@File : PageAction.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
------------------------------------
"""
from selenium.webdriver.support.wait import WebDriverWait

from KeyWordDriverTestFrameWork.config.VarConfig import iePath, chromePath
from KeyWordDriverTestFrameWork.util.DirAndTime import DirAndTime
from KeyWordDriverTestFrameWork.util.ObjectMap import get_element
from KeyWordDriverTestFrameWork.util.ClipboardUtil import Clipboard
from KeyWordDriverTestFrameWork.util.KeyBoardUtil import KeyBoardKeys
from KeyWordDriverTestFrameWork.util.WaitUntil import WaitUnit

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = None
waitUtil = None

# 首页-销售信息-商品状态(查看，已摘牌等选择一个点击)
def goods_state_chose_one(state):
    state = str(state)
    try:
        for i in range(1,15):
            i = str(i)
            by = 'xpath'
            loc = '/html/body/div[7]/div/div/div[1]/div[2]/div[2]/table/tbody/tr['+i+']/td[12]/a'
            print(loc)
            ele = get_element(driver,by,loc)
            print('是查看吗： ',ele.text)
            if ele.text == state:
                ele.click()
                break
    except Exception as e:
        raise e



# 打开浏览器
def open_browser(browser):
    global driver, waitUtil
    try:
        if browser.lower() == 'ie':
            driver = webdriver.Ie(executable_path=iePath)
        elif browser.lower() == 'chrome':
            driver = webdriver.Chrome()
        else:
            # driver = webdriver.Firefox(executable_path=fireFox)
            driver = webdriver.Chrome()
    except Exception as e:
        raise e
    else:
        waitUtil = WaitUnit(driver)  # driver 创建之后， 创建等待类实例对象


# 浏览器窗口最大化
def maximize_browser():
    try:
        driver.maximize_window()
    except Exception as e:
        raise e


# 加载网址
def load_url(url):
    try:
        driver.get(url)
    except Exception as e:
        raise e


# 强制等待
def sleep(num):
    num = int(num)
    try:
        import time
        time.sleep(num)
    except Exception as e:
        raise e


# 清除输入框的内容
def clear(by, locator):
    try:
        get_element(driver, by, locator).clear()
    except Exception as e:
        raise e


# 输入框中输入内容
def input_value(by, locator, value):
    value = str(value)
    try:
        element = get_element(driver, by, locator)
        element.click()
        element.send_keys(value)
    except Exception as e:
        raise e


# 点击操作
def click_btn(by, locator):
    try:
        get_element(driver, by, locator).click()
    except Exception as e:
        raise e


# 断言页面的title
def assert_title(title):
    try:
        assert title in driver.title, "%s not found in title!" % title
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e


# 断言目标字符串是否包含在页面源码中
def assert_string_in_page_source(string):
    try:
        assert string in driver.page_source, "%s not found in page source!" % string
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

# def assert_string_in_page_source(string):
#     try:
#         .assertIn(string,driver.page_source, "%s not found in page source!" % string)
#     except AssertionError as e:
#         raise AssertionError(e)
#     except Exception as e:
#         raise e
# 断言目标字符串不包含在页面源码中
def assert_string_not_in_page_source(string):
    try:
        assert string not in driver.page_source, "%s found in page source!" % string
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e

def assert_error_info(by, locator, string):
    element = get_element(driver, by, locator)
    text = element.text
    assert text == string


# 获取当前页面的title
def get_title():
    try:
        return driver.title
    except Exception as e:
        raise e

# 断言该元素位置信息是否正确
def assert_ele_text(by,loc,text):
    te = get_element(driver,by,loc).text
    assert text==te



# 获取页面源码
def get_page_source():
    try:
        return driver.page_source
    except Exception as e:
        raise e


# 切换到frame里面
def switch_to_frame(by, locator):
    try:
        driver.switch_to.frame(get_element(driver, by, locator))
    except Exception as e:
        raise e


# 跳到默认的frame
def switch_to_default():
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e


# 模拟ctrl+v键
def ctrl_v(value):
    try:
        Clipboard.set_text(value)
        sleep(2)
        KeyBoardKeys.two_keys('ctrl', 'v')
    except Exception as e:
        raise e


# 模拟tab键
def tab_key():
    try:
        KeyBoardKeys.one_key('tab')
    except Exception as e:
        raise e


# 模拟enter键
def enter_key():
    try:
        KeyBoardKeys.one_key('enter')
    except Exception as e:
        raise e


# 屏幕截图
def save_screen_shot():
    picture_name = DirAndTime.create_picture_path() + '//' + DirAndTime.get_current_time() + '.png'
    try:
        driver.get_screenshot_as_file(picture_name)
    except Exception as e:
        raise e
    else:
        return picture_name

# 点击弹框确认按钮
def click_popup_box_ok():
    try:
        #driver.accept()
        #switch_to_default()
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert.accept()
    except Exception as e:
        raise e
# 进入弹框
def check_popup_box_text():
    try:
        # 等待alert弹出框可见
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        # 从html页面切换到alert弹框
        # te = alert.text
        # print(te)
        # assert text in te
    except Exception as e:
        raise e
# 弹框断言
def assert_alert_text(string):
    try:
        sleep(2)
        a = driver.switch_to.alert
        text = a.text
        print(a.text)
        assert string in text, "%s not found in page source!" % string
    except AssertionError as e:
        raise AssertionError(e)
    except Exception as e:
        raise e
# 切换到新窗口并断言后退出窗口
def switch_window_check_text(string):
    """
    切换window窗口,切换一次后退出
    :return: 无
    """
    curHandle = driver.current_window_handle #获取当前窗口聚丙
    allHandle = driver.window_handles #获取所有聚丙　　　　　　　　　
    # """循环判断，只要不是当前窗口聚丙，那么一定就是新弹出来的窗口，这个很好理解。"""
    for h in allHandle:
        if h != curHandle:
            driver.switch_to.window(h) #切换聚丙，到新弹出的窗口
            text = get_page_source()
            assert string in text
            break



def enter_new_window():
    '''
    进入新的窗口
    :return:
    '''
    curHandle = driver.current_window_handle #获取当前窗口聚丙
    allHandle = driver.window_handles #获取所有聚丙　　　　　　　　　        "
    # ""循环判断，只要不是当前窗口聚丙，那么一定就是新弹出来的窗口，这个很好理解。"""
    for h in allHandle:
        if h != curHandle:
            driver.switch_to.window(h) #切换聚丙，到新弹出的窗口

def get_all_text():
    try:
        print(get_page_source())
    except Exception as e:
        raise e


# 判断数据测试数据够不够，不够添加
def add_data(needNum,addNum,):
    pass
# 添加企业资质信息
def gdce_upLoad_file():
    try:
        upload_element = driver.find_element_by_xpath('//*[@id="upLoadFile"]')
        sleep(3)  # 为了看效果
        upload_element.send_keys(r'/Users/Shared/Relocated Items/Security/长期文件/自动化测试/KeyWordDriverTestFrameWork/exceptionpictures/2019-08-03/15_20_15.png')
    except Exception as e:
        raise e

def wait_presence_of_element_located(by, locator):
    """显示等待页面元素出现在DOM中，单并不一定可见"""
    waitUtil.presence_of_element_located(by, locator)


def wait_frame_to_be_available_and_switch_to_it(by, locator):
    """检查frame是否存在，存在就切换到frame中"""
    waitUtil.frame_to_be_available_and_switch_to_it(by, locator)


def wait_visibility_of_element_located(by, locator):
    """显示等待页面元素出现在DOM中，并且可见"""
    waitUtil.visibility_of_element_located(by, locator)


# 关闭浏览器
def quit_browser():
    try:
        driver.quit()
    except Exception as e:
        raise e
# 关闭当前窗口
def close_browser():
    try:
        driver.close()
    except Exception as e:
        raise e

# 刷新当前页面
def refresh_current_page():
    try:
        driver.refresh()
    except Exception as e:
        raise e
# 获取当前页面url，新页面打开该url
def new_page_open_url():
    try:
        url = driver.current_url
        load_url(url)
    except Exception as e:
        raise e





if __name__ == '__main__':
    open_browser('firefox')
    load_url('http://126.com')
    #inputValue('id', 'kw','python')
    # clear('id', 'kw')
    # inputValue('id', 'kw', 'python')
    # clickBtn('id', 'su')
    # sleep(3)
    # title = getTitle()
    # print(title)
    # assertTitle('python')
    # assert_string_in_page_source('python')
    ctrl_v('python')
