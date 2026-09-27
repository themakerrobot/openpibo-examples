from openpibo.collect import News

news = News()

result = news.search('경제')

print(result)
# print(result[0]['title'])