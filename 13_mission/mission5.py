#웹크롤링(CSV 파일) + 데이터분석(전처리, 그래프)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

r1 = requests.get('https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page=1&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N', headers=headers)

soup1 = BeautifulSoup(r1.text, 'html.parser')

r2 = requests.get('https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page=2&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N', headers=headers)

soup2 = BeautifulSoup(r2.text, 'html.parser')

r3 = requests.get('https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page=3&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N', headers=headers)

soup3 = BeautifulSoup(r3.text, 'html.parser')

r4 = requests.get('https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page=4&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N', headers=headers)

soup4 = BeautifulSoup(r4.text, 'html.parser')

trs1 = soup1.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')
trs2 = soup2.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')
trs3 = soup3.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')
trs4 = soup4.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')

s=[]

for tr in trs1:
    rank = tr.select_one('td.number').text[0:2]
    title = tr.select_one('a.title.ellipsis').text
    album = tr.select_one('a.albumtitle.ellipsis').text
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])
    print(rank, title, album)

for tr in trs2:
    rank = tr.select_one('td.number').text[0:2]
    title = tr.select_one('a.title.ellipsis').text
    album = tr.select_one('a.albumtitle.ellipsis').text
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])


for tr in trs3:
    rank = tr.select_one('td.number').text[0:2]
    title = tr.select_one('a.title.ellipsis').text
    album = tr.select_one('a.albumtitle.ellipsis').text
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])


for tr in trs4:
    rank = tr.select_one('td.number').text[0:2]
    title = tr.select_one('a.title.ellipsis').text
    album = tr.select_one('a.albumtitle.ellipsis').text
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    album = re.sub('[^0-9a-zA-Zㄱ-힗]', '', album)
    title = title.replace('TITLE', '')

    s.append([rank, title, album])



# df = pd.DataFrame(s, columns=['순위', 'Title명', '앨범명'])
# df.to_csv('seventeen.csv', index=False)

