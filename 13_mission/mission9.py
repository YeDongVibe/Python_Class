# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

driver = webdriver.Chrome()

url = 'https://www.genie.co.kr/detail/artistSong?xxnm=14945871'
driver.get(url)
driver.implicitly_wait(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')

trs = soup.select('#songlist-box > div.music-list-wrap > table > tbody > tr')

for tr in trs :
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('a.title.ellipsis').text.strip()
    album = tr.select_one('a.albumtitle.ellipsis').text.strip()
    title = title.replace('TITLE', '')
    print(rank, title, album, sep='|')