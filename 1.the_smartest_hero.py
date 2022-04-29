import requests

superhero_list = ['Hulk', 'Captain America', 'Thanos']

# 1. Вывод всех запрашиваемых супергероев со значениями intelligence


def heroes_dict(hero_list):
    hero_intelligence = {}
    for hero in hero_list:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        response = requests.get(url)
        same_heroes = response.json()['results']
        for same_hero in same_heroes:
            if same_hero['name'] == hero:
                hero_intelligence[hero] = same_hero['powerstats']['intelligence']
    print(hero_intelligence)


# if __name__ == '__main__':
#     heroes_dict(superhero_list)


# 2. Вывод супергероя с наибольшим значением intelligence из запрашиваемого списка

def the_smartest_hero(hero_list):
    max_intelligence = 0
    hero_name = ''
    for hero in hero_list:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        response = requests.get(url)
        same_heroes = response.json()['results']
        for same_hero in same_heroes:
            if same_hero['name'] == hero:
                hero_max_intelligence = same_hero['powerstats']['intelligence']
        if int(hero_max_intelligence) > max_intelligence:
            max_intelligence = int(hero_max_intelligence)
            hero_name = hero
    print(f'{hero_name} - самый умный супергерой со значением intelligence = {max_intelligence}.')

if __name__ == '__main__':
    the_smartest_hero(superhero_list)