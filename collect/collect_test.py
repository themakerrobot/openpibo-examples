from openpibo.collect import Wikipedia
from openpibo.collect import Weather
from openpibo.collect import News


def run():
  # 위키 검색
  wiki = Wikipedia()
  result = wiki.search('사과')
  print('=== Wikipedia ===')
  print('Result:', result['0'])

  # 날씨 검색
  weather = Weather()
  result = weather.search('서울')
  print('\n\n=== Weather ===')
  print('Keyword:', Weather.region_list.keys())
  print('Result:', result)

  # 뉴스 검색
  news = News()
  result = news.search('경제')
  print('\n\n=== News ===')
  print('Keyword:', News.topic_list.keys())
  print('Result:', result)

if __name__ == "__main__":
  run()
