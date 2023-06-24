import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

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

        result = f'{rank} {title} {album}'
        result = ' '.join(result.split())
        s.append(result)
        print(result)
print(s)      

df = pd.DataFrame(s, columns=['데이터'])
df.to_csv('seventeen.csv', index=False)

# df = pd.DataFrame(s, columns=['순위', 'Title명', '앨범명'])
# print(df)
# df.to_csv('seventeen.csv', encoding='utf-8')
# print('CSV 파일로 저장되었습니다.')

# df = pd.read_csv('seventeen.csv')
# df[['순위', 'title명', '앨범명']] = df['데이터'].str.extract(r'^(\d+)\s(.*?)(\s.*)?$')
# df.to_csv('seventeen_modified.csv', columns=['순위', 'title명', '앨범명'], index=False)