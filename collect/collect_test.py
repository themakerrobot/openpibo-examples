from openpibo.collect import *

# 위키피디아 스크래핑
wiki = Wikipedia()
wiki.search('강아지')
print(wiki)

# 날씨 데이터 가져오기
weather = Weather()
weather.search('서울')
print(weather)

# 뉴스 가져오기
news = News()
news.search('경제')
print(news)
