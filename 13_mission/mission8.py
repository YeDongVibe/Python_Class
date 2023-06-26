#웹크롤링(CSV 파일) + 데이터분석(전처리, 그래프)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

response = requests.get('https://www.genie.co.kr/detail/artistSong?xxnm=14945871', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

trs = soup.select('#songlist-box > div.music-list-wrap > table > tbody > tr')
s=[]
for tr in trs:
    rank = tr.select_one('td.number').text[0:2].strip()
    title = tr.select_one('a.title.ellipsis').text.strip()
    album = tr.select_one('a.albumtitle.ellipsis').text.strip()
    # title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    # album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])
    print(rank, title, album)

df = pd.DataFrame(s, columns=['순위', 'Title명', '앨범명'])
print(df)
df.to_csv('seventeen2.csv', index=False)

