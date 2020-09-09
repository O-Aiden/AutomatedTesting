#! /usr/bin/python
# coding:utf-8
"""
@creator:Bingo.he
@modifier:Yuki
@file: gen_common_kw.py
@time: 2020/09/09
"""
import os
import re
# from apitest.Common.Testscript.utils.logger import logger
from apitest.Common.Testscript.utils.operate_xls import *


class GenRFkw:
    def __init__(self, xls_folder, demo_case_folder):
        '''

        :param xls_folder: 存放excel文件的文件夹路径
        :param demo_case_folder: 存放.robot文件的文件夹路径
        '''
        self.xls_folder = xls_folder
        self.target_case_folder = demo_case_folder

    # 引入接口测试的包
    @staticmethod
    def kw_requests_init(target_robot_name):
        with open(target_robot_name, 'a') as f:
            f.write('*** Settings ***' + '\n')
            f.write('Library           TestLibrary' + '\n')
            f.write('Library           RequestsLibrary' + '\n')
            f.write('\n')
            f.write('*** Keywords ***' + '\n')

    @staticmethod
    def gen_kw(target_robot_name, param_type, req_method, url, document, headers, msg_type):
        if param_type == "json" or param_type == "data":
            # param_type = "data"
            param_type = "json"
        with open(target_robot_name, 'a', encoding="utf-8") as f:
            f.write('    [Arguments]    ${url}')
            f.write('    ${' + param_type + '}')

            # 允许url中传递可变参数
            if "${" in url:
                p = re.compile(r'{(.*?)}')
                verify_urls = p.findall(url)
                for verify_url in verify_urls:
                    f.write("    ${{{}}}".format(verify_url))

            # 允许headers中传递可变参数
            if "${" in headers:
                sprint_str = headers
                p = re.compile(r'{(.*?)}')
                sprint_num = p.findall(sprint_str)
                for s in sprint_num:
                    f.write("    ${{{}}}".format(s))
            f.write('\n')

            f.write('    [Documentation]   ' + document + '\n')

            # 兼容form-data请求
            if "multipart/form-data" == msg_type:
                f.write('    ${boundary}=    xl boundary parse    ${data}' + '\n')

            f.write('    ${headers}    Create Dictionary    ' + headers + '\n')
            f.write('    Create Session    api    ${url}    ${headers}   verify=${False}' + '\n')
            if '' != param_type.strip():  # 接口输入参数个数不为零
                if req_method.upper() == 'GET' or req_method.upper() == 'DELETE':  # .upper()将所有字母转为答谢大写
                    f.write('    ${{Ret}}    {} Request   api   '.format(req_method.capitalize()) + url)
                    f.write('${' + param_type + '}')  # 发送GET请求，直接把EXCEL中读取出来的参数连接到URL后面
                    f.write('\n')
                else:
                    f.write('    ${{Ret}}    {} Request   api   '.format(req_method.capitalize()) + url) # .capitalize()将第一个字母变大
                    f.write('    ' + param_type + '=${' + param_type + '}')
                    f.write('\n')
            f.write('    [Return]    ${Ret}' + '\n')
            f.write('\n')

    @staticmethod
    def find_file_name(file_dir):
        files = None
        for root, dirs, files in os.walk(file_dir):
            #print("file_dir: "+file_dir)
            #print("当前目录路径" + root)
            #print("当前路径下所有子目录" + str(dirs))
            #print("当前路径下所有非目录子文件" + str(files))
            # logger.info("当前目录路径" + root)  # 当前目录路径
            # logger.info("当前路径下所有子目录" + str(dirs))  # 当前路径下所有子目录
            # logger.info("当前路径下所有非目录子文件" + str(files))  # 当前路径下所有非目录子文件
            files = [file for file in files if ".xlsx" in file]
            #print("files:",files)
            # 按照顺序排序
            files.sort()
        return files

    @staticmethod
    def interface_name(kw_excel):
        return kw_excel.split(".")[0]

    def run(self, **kwargs):
        # 找到excel文件的路径
        xls_files = self.find_file_name(self.xls_folder)
        #print("xls_files: ",xls_files)
        target_robot_name = os.path.join(self.target_case_folder, "DT_Hb_kwRequests.robot")

        if os.path.exists(target_robot_name):
            os.remove(target_robot_name)
        # 引入包
        self.kw_requests_init(target_robot_name)
        # 循环读取所有的excel文件
        for xls_file in xls_files:
            # Excel文件名称规则： 接口服务名称和path的组合
            # 关键字命名规则：公司代号_流水线（项目组）代号_Excel的前缀
            interface_name = self.interface_name(xls_file)
            with open(target_robot_name, 'a') as f:
                f.write('DT_Hb_' + interface_name + '\n')
            #print("a: ",os.path.join(self.xls_folder, xls_file))
            book = ReadRFExcel(os.path.join(self.xls_folder, xls_file), 0)
            #print("book: ",book)
            param_type = book.rf_xls_msg_type()
            # param = book.rf_xls_param_value()
            decode_type = book.rf_xls_msg_type()
            url = book.rf_xls_url()
            document = book.rf_xls_document()
            headers = book.rf_xls_headers()
            method = book.rf_xls_method()
            self.gen_kw(target_robot_name, param_type, method, url, document, headers, decode_type)

if __name__ == '__main__':
    test = GenRFkw("apitest/Common/Testscript/data","apitest/Common/Testscript/robot")
    test.run()