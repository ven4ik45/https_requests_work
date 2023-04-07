unicodedata = 'utf-8'
import requests
import json


url = 'https://akabab.github.io/superhero-api/api'
all_heroes = '/all.json'
need_heroes = ['Hulk', 'Captain America', 'Thanos']

data = requests.get(url+all_heroes).content
cont = json.loads(data)


def get_heroes(content, need_heroes):
    heroes_dict = {}
    for n in content:
        for h in need_heroes:
            if h == n['name']:
                heroes_dict[n['name']] = n['powerstats']['intelligence']
    return heroes_dict


def return_smartest_hero(heroes):
    for k, v in heroes.items():
        if v == max(heroes.values()):
            return k


heroes = get_heroes(cont, need_heroes)
smartest_hero = return_smartest_hero(heroes)
print(f'Cамый умный из трех супергероев (Hulk, Captain America, Thanos): {smartest_hero}')
