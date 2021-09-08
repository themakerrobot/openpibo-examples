from openpibo.collect import *


wiki = Wikipedia()
wiki.search('강아지')
print(wiki)

weather = Weather()
weather.search('서울')
print(weather)

news = News()
news.search('경제')
print(news)