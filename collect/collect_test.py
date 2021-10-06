from openpibo.collect import Wikipedia, Weather, News

wiki = Wikipedia().search('사과')
print('=== Wikipedia ===')
print('Result:', wiki['0'])

weather = Weather().search('서울')
print('\n\n=== Weather ===')
print('Keyword:', Weather.region_list.keys())
print('Result:', weather)

news = News().search('경제')
print('\n\n=== News ===')
print('Keyword:', News.topic_list.keys())
print('Result:', news)
