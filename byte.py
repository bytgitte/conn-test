#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 上午12:58
# @Email   : recruits@bytedance.com

import hashlib,time,requests,os
import random,ssl,getopt,queue
import threading,datetime
import sys,re,sqlite3,lxml,urllib3
from bs4 import BeautifulSoup as BS


# Check py version
pyversion = sys.version.split()[0]
if pyversion <= "3":
    exit('Need python version 3.x')
