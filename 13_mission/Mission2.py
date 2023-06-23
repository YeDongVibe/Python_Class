#웹크롤링(CSV 파일) + 데이터분석(전처리, 그래프)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

url = 'https://www.melon.com/search/song/index.htm?q=%EC%84%B8%EB%B8%90%ED%8B%B4&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=#params%5Bq%5D=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&params%5Bsort%5D=hit&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&params%5BmwkLogType%5D=T&po=pageObj&startIndex=1'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

s=[]

rank = soup.find_all("")