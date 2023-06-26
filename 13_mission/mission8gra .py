import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('seventeen2.csv', encoding='utf-8')

album_counts = df['앨범명'].value_counts()

plt.rcParams['font.family'] = 'Malgun Gothic'


colors = ['black', '#ED95E1', 'gray', '#F2E1BA', '#EDB120', 'yellow', 'red', '#00DCF4' , 'lightblue', 'blue', '#D3A5FF', '#00FFF2', 'brown', 'green', 'silver', 'lightpink', '#00BA91', '#000B84', '#8EF0FF', '#E0BB7B']


plt.figure(figsize=(10, 6))
plt.barh(album_counts.index, album_counts, color=colors)
plt.title('앨범별 분포')
plt.xlabel('Count')
plt.ylabel('Albums')
plt.tight_layout()

plt.show()
