#웹크롤링(CSV 파일) + 데이터분석(전처리, 그래프)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get('https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page=1&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

trs = soup.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')
s=[]
for tr in trs:
    rank = tr.select_one('td.number').text[0:2]
    title = tr.select_one('a.title.ellipsis').text
    album = tr.select_one('a.albumtitle.ellipsis').text
    # rank = re.sub('[^0-9a-zA-Zㄱ-힗]', '', rank)
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])
    print(rank, title, album)

df = pd.DataFrame(s, columns=['순위', 'Title명', '앨범명'])
df.to_csv('seventeen.csv', index=False)

