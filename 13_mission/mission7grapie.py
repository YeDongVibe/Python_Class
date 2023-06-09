import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('seventeen2.csv', encoding='utf-8')

# Count the occurrences of each album name
album_counts = df['앨범명'].value_counts()
print(album_counts.value_counts)

plt.rcParams['font.family'] = 'Malgun Gothic'


# Plot the pie chart
plt.figure(figsize=(8, 6))
plt.pie(album_counts, labels=album_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Albums')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
