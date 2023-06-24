import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# ChromeDriver 설정
ser = Service('C:/Users/wkwhs/Downloads/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=ser)

# URL 정의
url = 'https://www.melon.com/search/song/index.htm?q=%EC%84%B8%EB%B8%90%ED%8B%B4&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=#params%5Bq%5D=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&params%5Bsort%5D=hit&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&params%5BmwkLogType%5D=T&po=pageObj&startIndex=1'

# 브라우저에서 URL 열기
driver.get(url)

# 페이지 소스 가져오기
html_melon = driver.page_source

# BeautifulSoup를 사용하여 HTML 파싱
soup = BeautifulSoup(html_melon, 'html.parser')

# 노래 정보가 포함된 테이블 행 찾기
songs = soup.select('tbody > tr')
print(songs)

for song in songs:
    title_elem = song.select_one('.fc_gray')
    album_elem = song.select_one('div.ellipsis.rank03 > a')

    if title_elem and album_elem:
        title = title_elem.text.strip()
        album = album_elem.text.strip()
        print(title, album)


# for song in songs:
#     title = song.select_one(".fc_gray").text
#     album = song.select_one('div.ellipsis.rank03 > a').text
#     #album = song.select_one(".fc_mgray").text
#     #print(title)
#     print(album)
# song_data = []
# rank = 1

# for song in songs:
#     title_elem = song.select_one('div.ellipsis.rank01 > span > a')
#     album_elem = song.select_one('div.ellipsis.rank03 > a')

#     if title_elem and album_elem:
#         title = title_elem.text.strip()
#         album = album_elem.text.strip()
#         mylist = ['melon', rank, title, album]
#         song_data.append(mylist)
#         rank += 1

#         print(song_data)

#브라우저 닫기
driver.quit()





# # 데이터 출력
# for rank, song in enumerate(rows, start=1):
#     title = song.select_one('.ellipsis.rank01 > span > a').text.strip()
#     album = song.select_one('.ellipsis.rank03 > a').text.strip()
#     print(f"Rank: {rank}, Title: {title}, Album: {album}")

