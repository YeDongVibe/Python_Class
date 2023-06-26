import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

s = []

for page in range(1, 5):
    url = f'https://www.genie.co.kr/search/searchSong?Coll=sAll&query=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&page={page}&pagesize=20&of=POPULAR&fscount=&Genre=&Country=&reQuery=&researchyn=N'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    trs = soup.select('#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr')

    for tr in trs:
        rank = tr.select_one('td.number').text[0:2].strip()
        title = tr.select_one('a.title.ellipsis').text.strip()
        album = tr.select_one('a.albumtitle.ellipsis').text.strip()

        if 'TITLE' in title:
            title = title.replace('TITLE', '')

        result = {
            '순위': rank,
            'Title명': title,
            '앨범명': album
        }
        s.append(result)

df = pd.DataFrame(s)
df['순위'] = df['순위'].str.strip()
df['Title명'] = df['Title명'].str.strip()
df['앨범명'] = df['앨범명'].str.strip()
df.to_csv('seventeen.csv', index=False)
