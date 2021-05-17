# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')
# print(resp)

soup = BeautifulSoup(resp, 'html.parser')
# print(soup)

movies = soup.find_all('dl', class_='lst_dsc')
# print(movies[0])

for movie in movies:
    # 영화제목 [평점]
    # ex) 스파이럴 [9.83]
    name = movie.find('a').text
    point = movie.find('span', class_='num').text
    print(name + ' [' + point + ']')