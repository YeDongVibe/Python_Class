# 네이버 블로그에서 특정 키워드에 대한 포스트 제목과 링크를 가져오는 예시
import requests
from bs4 import BeautifulSoup

# 네이버 블로그에서 키워드 "파이썬"에 대한 포스트 검색 페이지에서 HTML 코드 가져오기
url = 'https://search.naver.com/search.naver'
params = {'query': '파이썬', 'where': 'blog'}
response = requests.get(url, params=params)
#print(response.url)

# HTML 코드 파싱하기
soup = BeautifulSoup(response.text, 'html.parser')

# 포스트 정보 태그 가져오기
posts = soup.select('.total_tit')

# 포스트 정보 출력하기
for post in posts:
    # 제목과 링크 가져오기
    title = post.text
    link = post.get('href')
    print(title)
    print(link)
    print('-' * 50)


#----------------------------------------------------------------------------------------------------------------------------
# 구글 뉴스의 제목과 링크를 출력하는 예시
import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.WwrzSb')
for title in titles:
    print(title.get('aria-label'))
    print('https://news.google.com' + title['href'][1:])
    print('-' * 50)



#----------------------------------------------------------------------------------------------------------------------------
# 다음 영화 예매 순위 정보를 출력하는 예시
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

rank_list = soup.select('div.thumb_cont > strong > a')
rank_rate = soup.select('span.txt_append > span > span')

for rank, title in enumerate(rank_list, 1):
    print(f'{rank}위: {title.text} : 예매율({rank_rate[rank-1].text})')

#----------------------------------------------------------------------------------------------------------------------------
# 다음 영화 예매 순위 정보를 출력하는 예시2
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

ol = soup.select_one('.list_movieranking')

li_list = ol.find_all('li')

# 데이터 프레임으로 변경
movie = []

for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1]
    mvdate = li.select_one('.txt_info > .txt_num').text

    movie.append([rank, name , see, grade, num,mvdate])

df = pd.DataFrame(movie, columns=['순위', '영화명', '관람연령', '평점', '예매율', '개봉일'])

df.to_csv('movie_info.csv', index=False, encoding='cp949')

df = pd.read_csv('C:\Ye_Dong\Python_Class\movie_info.csv', encoding='cp949')
df.sort_values('평점', ascending=False)

df['개봉일'] = pd.to_datetime(df['개봉일'], format="%y.%m.%d")
df.head()


#----------------------------------------------------------------------------------------------------------------------------
# 한국은행의 기준금리 정보를 가져오는 예시
import requests
from bs4 import BeautifulSoup

url = 'https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

#rate = soup.select_one('#content > div.table.tac > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
#rate = soup.select('#content > div.table.tac > table > tbody > tr > td:nth-child(3)')[0].text
rate = soup.select('#content > div.table.tac > table > tbody > tr > td')[2].text
print(f'기준금리: {rate}')

