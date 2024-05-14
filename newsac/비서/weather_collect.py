from openpibo.collect import Weather

weather = Weather()

result = weather.search('서울')

print(result)
print(result['today'])