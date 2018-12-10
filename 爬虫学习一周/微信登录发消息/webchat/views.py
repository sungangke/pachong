from django.shortcuts import render,HttpResponse
import  requests
import time
import re
import json
from bs4 import BeautifulSoup

def index_login(req):
    """
    访问https://wx.qq.com
    :param req:登录地址
    :return:返回页面二维码
    """
    