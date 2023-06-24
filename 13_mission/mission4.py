import requests
from bs4 import BeautifulSoup
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

url = 'https://www.melon.com/search/song/index.htm?q=%EC%84%B8%EB%B8%90%ED%8B%B4&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=#params%5Bq%5D=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&params%5Bsort%5D=hit&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&params%5BmwkLogType%5D=T&po=pageObj&startIndex=1'

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

# 웹 페이지에서 순위, 곡명, 앨범을 추출
rank_list = soup.find_all("span", class_="rank")
song_list = soup.find_all("div", class_="ellipsis rank01")
album_list = soup.find_all("div", class_="ellipsis rank03")

# 결과 출력
for rank, song, album in zip(rank_list, song_list, album_list):
    print(rank.text.strip(), song.text.strip(), album.text.strip())
