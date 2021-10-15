from openpibo.edu_v1 import Pibo

def run():
  result = pibo.search_wikipedia("강아지")
  print("== Wikipedia ==\n", result)

  result = pibo.search_weather("전국")
  print("\n\n== Weather ==\n", result)

  result = pibo.search_news("속보")
  print("\n\n== News ==\n", result)

if __name__ == "__main__":
  pibo = Pibo()

  run()
