# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=')

soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

webtoons = soup.find('ul', class_='img_list')
# print(webtoons)

dl = webtoons.select('dl')
# print(dl[0])

lst = list()

for webtoon in dl:
    # print(webtoon)
    # name = webtoon.find('dt').text
    title = webtoon.find('a')['title']
    point = webtoon.find('strong').text
    # print('{} [{}]'.format(title ,point))
    
    tmp = {}
    tmp['title'] = title
    tmp['star'] = point
    lst.append(tmp)
    
# print(lst)

res = {}
res['webtoons'] = lst
# print(res)

res_json = json.dumps(res, ensure_ascii=False)
# print(res_json)
with open('webtoons.json', 'w', encoding='utf-8') as f:
    f.write(res_json)