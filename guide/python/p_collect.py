from openpibo.collect import Wikipedia
from openpibo.collect import Weather
from openpibo.collect import News

wikipedia = Wikipedia()
weather = Weather()
news = News()

print('## 위키피디아')
result = wikipedia.search('로봇')
print(result['0']['content'])

print('## 날씨')
result = weather.search('서울')
print(result)

print('## 뉴스')
result = news.search('속보')
print(result[0]['title'])