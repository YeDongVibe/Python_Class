import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

url = 'https://www.melon.com/search/song/index.htm?q=%EC%84%B8%EB%B8%90%ED%8B%B4&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=#params%5Bq%5D=%25EC%2584%25B8%25EB%25B8%2590%25ED%258B%25B4&params%5Bsort%5D=hit&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&params%5BmwkLogType%5D=T&po=pageObj&startIndex=1'

r = requests.get(url, headers=headers)

html = r.text

soup = BeautifulSoup(html, "html.parser")


trs = soup.select("#frm_defaultList > div > table > tbody > tr")
s = []

for tr in trs:
    rank = tr.select_one("div").text[0:2]
    title = tr.select_one("a.fc_gray").text
    album = tr.select_one("a")

    print(rank)

# rank = soup.select("#frm_defaultList > div > table > tbody > tr:nth-child(1) > td.no > div")
# title = soup.select("#frm_defaultList > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > a.fc_gray")
# album = soup.select("#frm_defaultList > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > div > a")

# for i in range(len(rank), len(title), len(album)):
#     rank[i] = rank[i].text[0:2]
#     title[i] = title[i].text
#     album[i] = album[i].text

    