#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os

import json
import time
import datetime
from importlib import reload

import requests
import hmac
import random
import string
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from base64 import b64encode

# from httprunner import __version__
from hashlib import sha256
import ipaddress
from xml.dom.minidom import parse
import xml.dom.minidom
import struct
import socket
from string import ascii_letters, digits
from random import choice


# def get_httprunner_version():
#     return __version__
# reload(sys)
# sys.en('utf8')

province_id = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,
               50,51,52,53,54,61,62,63,65,65,81,82,83]

def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


# 获取captchaSign
def get_captcha_sign(username, password):
    return sha256(
        username.encode("utf-8") + get_password(password).encode("utf-8") + "0000".encode("utf-8")).hexdigest()


# sha256加密密码
def get_password(password):
    return sha256(password.encode("utf-8")).hexdigest()


def get_cookie(username, password):
    # username = "admin-wsc"
    # password = "Yingzi125@"
    cookie = "SESSION=" + get_session(username, password)
    return cookie


def get_session(username, password):
    # username = "admin-wsc"
    # password = "Yingzi125@"
    url = "http://139.198.116.76:8000/api/home/test/login"
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    payload = {
        "captcha": "0000",
        "captchaSign": get_captcha_sign(username, password),
        "emailCaptcha": "",
        "openId": "",
        "openUserName": "",
        "password": "",
        "username": username
    }
    res = requests.post(url, json=payload, headers=headers)
    cookie = res.headers['Set-Cookie']
    print(cookie)
    str1 = "="
    str2 = ";"
    session = cookie[cookie.index(str1) + 1:cookie.index(str2)]
    return session


# 获取加密公钥
def get_pubkey():
    url = "http://139.198.116.76:8000/api/home/publicKey"
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    res = requests.get(url, headers=headers)
    pubkey = res.content
    return json.loads(pubkey)['data']['publicKeyPem']


# 加密密码
def get_encrypt_password(password):
    key = serialization.load_pem_public_key(get_pubkey().replace("\r\n", "\n").encode())
    enc_password = key.encrypt(password.encode("utf-8"),
                               padding=padding.OAEP(mgf=padding.MGF1(hashes.SHA1()), algorithm=hashes.SHA256(),
                                                    label=None))
    return b64encode(enc_password).decode("utf-8")


# 获取文件
def get_file():
    print('11')


# def get_prefix():
#     subPrefix = "88.408."
#     suffix = get_random_param(10000000, 1000000000000)
#     prefix = subPrefix + str(suffix)
#     return prefix


# def get_prefix():
#     return "88.502.4321"


def get_cookie1():
    return "MmFiNmZkZDQtNjJiMS00ZDIwLWFjZjMtMTY3ZDQ1ZjYxMjZk"


def get_username():
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(32)]
    random_str = ''.join(str_list)
    return random_str


def get_mobile():
    str = "1"
    for i in range(10):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    return str


def get_email():
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(16)]
    random_str = ''.join(str_list)
    random_str = random_str + "@qaqseq.com"
    return random_str


def get_dict(value):
    list2 = []
    for i in range(value):
        list1 = [i]
        list2.append(list1)
    print(list2)
    print(len(list2))
    return list2


def get_join_str(str1, str2):
    str = str1 + "," + str2
    return str


# 生成随机数字
def get_random_param(min, max, count=3):
    random_list = []
    for i in range(count):
        random_list.append(random.randint(min, max))
    return random_list[0]


def hook_down(response):
    filename = response.headers['Content-Disposition'].split(';')[1].replace("filename=", "")

    path = os.path.dirname(os.path.abspath(__file__))

    # filename.decode('utf-8')
    out_file = open(path + "/download/" + filename, 'wb')
    data = response.body
    out_file.write(data)


def hook_example():
    sleep(30)


def setup_hook_example():
    sleep(80)

def setup_hook_example1():
    sleep(1)

def setup_hook_example20():
    sleep(20)
def setup_hook_example30():
    sleep(30)

def ran1():
    #  随机生成年月日
    yea = random.randint(1933, int(time.strftime("%Y")))  # 生成年
    #  生成月
    mon = random.randint(1, 12)
    ran_mon = '0' + str(mon) if mon < 10 else mon
    #  生成日
    day = random.randint(1, 27)
    ran_day = '0' + str(day) if day < 10 else day
    return str(yea) + str(ran_mon) + str(ran_day)


def ran_value():
    #  生成年月日后的三位数
    value = random.randint(10, 199)
    if value < 100:
        return "0" + str(value)
    else:
        return str(value)


def ran_area():
    #  随机取生成前六位
    province = (
        '11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42',
        '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')
    return str(province[random.randint(0, len(province))] + '0101')


def get_random_ipv6():
    str_ip = str(ipaddress.IPv6Address(random.randint(0, 2 ** 128 - 1)))
    return str_ip


def get_random_port():
    random_port = random.randint(0, 65535)
    return random_port


def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
    writer.write(indent + "<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()


def str_to_int(arg):
    return int(arg) + 1


def str_to_int2(arg):
    return int(arg) + 2
def str_to_int4(arg):
    return int(arg) + 4


# 调整xml格式
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
    writer.write(indent + "<" + self.tagName)
    attrs = self._get_attributes()
    a_names = attrs.keys()
    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        xml.dom.minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
                and self.childNodes[0].nodeType == xml.dom.minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not xml.dom.minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))


# 批量产生500条xml标识数据到xml文件
def batch_generate_xml_data(path, cnt):
    dom_tree = xml.dom.minidom.parse(path)
    collection = dom_tree.documentElement
    items_list = collection.getElementsByTagName("items")
    items = items_list[0]
    for i in range(cnt):
        item = dom_tree.createElement('item')
        identity = dom_tree.createElement('identity')
        identity.appendChild(dom_tree.createTextNode("88.502.119/zjtest927-" + str(i)))
        terminal_type = dom_tree.createElement('terminalType')
        terminal_type.appendChild(dom_tree.createTextNode("terminalType" + str(i)))
        subject = dom_tree.createElement('subject')
        subject.appendChild(dom_tree.createTextNode("subject" + str(i)))
        item.appendChild(identity)
        item.appendChild(terminal_type)
        item.appendChild(subject)
        items.appendChild(item)
    f = open(path, "w")
    dom_tree.writexml(f, addindent='\t', newl='\n', encoding='UTF-8')
    f.close()

def get_birthday():
    # 随机生成年月日
    year = random.randint(1960, 2000)
    month = random.randint(1, 12)
    # 判断每个月有多少天随机生成日
    if year % 4 == 0:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 29)
    else:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
    # 小于10的月份前面加0
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    birthday = str(year) + str(month) + str(day)
    return birthday


def get_idcardno():
    id_num = ''
    # 随机选择地址码
    id_num += str(random.choice(province_id))
    # 随机生成4-6位地址码
    for i in range(4):
        ran_num = str(random.randint(0, 9))
        id_num += ran_num
    b = get_birthday()
    id_num += b
    # 生成15、16位顺序号
    num = ''
    for i in range(2):
        num += str(random.randint(0, 9))
    id_num += num
    # 通过性别判断生成第十七位数字 男单 女双
    s = '男'
    print("性别:", s)
    if s == '男':
        # 生成奇数
        seventeen_num = random.randrange(1, 9, 2)
    else:
        seventeen_num = random.randrange(2, 9, 2)
    id_num += str(seventeen_num)
    eighteen_num = str(random.randint(1, 10))
    if eighteen_num == '10':
        eighteen_num = 'X'
    id_num += eighteen_num
    return id_num


if __name__ == "__main__":
    # print(get_cookie("admin-wsc", "Yingzi125@"))
    # print(get_session("admin-wsc", "Yingzi125@"))
    # print(get_captcha_sign("admin-wsc", "59f16d4c00343e8a3814fbd2488b94e076ce28d27c90e5883b3f1145024894c2"))
    # print(get_idcardno())
    # print(get_prefix())
    # xml.dom.minidom.Element.writexml = fixed_writexml
    # batch_generate_xml_data("/Users/graypig/Documents/teleinfoautotest/data/88.502.119_zjauto9537.xml", 5)
    # print(get_dict( 500000))
    print(get_prefix())


def get_day():
    now = datetime.datetime.now()
    return now.day


def get_yestoday():
    now = datetime.datetime.now() - datetime.timedelta(days=1)
    return now.day


def get_date():
    now = datetime.datetime.now()
    return now.date


def get_prefix_10(prefix):
    return [
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))},
        {prefix + str(get_random_param(10000, 20000, 10))}
    ]

