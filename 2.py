from collections import ChainMap
from random import randint


def get_damage(unit, damage):
    damage = damage - unit['armor']
    if damage > 0:
        unit['HP'] -= damage


rome_soldiers = {
    'country': 'Rome',
    'HP': 100,
    'armor': 10,
    'damage': 25,
    'type': 'пехота',
    'coords': None
}

archer = {
    'HP': 50,
    'armor': 10,
    'damage': 100,
    'type': 'лучник'
}

heavy_soldier = {
    'HP': 150,
    'armor': 30,
    'damage': 50,
    'type': 'бронированный пехотинец'
}

light_soldier = ChainMap({}, rome_soldiers)
archer1 = ChainMap({}, archer, rome_soldiers)
heavy_soldier1 = ChainMap({}, heavy_soldier, rome_soldiers)
heavy_soldier2 = ChainMap({}, heavy_soldier, rome_soldiers)

print('light_soldier :', light_soldier, end='\n\n')
print('archer1 :', archer1, end='\n\n')
print('heavy_soldier1 :', heavy_soldier1, end='\n\n')
print('heavy_soldier2 :', heavy_soldier2, end='\n\n')

print('наносим 50 единиц урона юнитам archer1 и heavy_soldier1:', end='\n\n')
get_damage(archer1, 50)
get_damage(heavy_soldier1, 50)

print('light_soldier :',  *light_soldier.items(), end='\n\n')
print('archer1 :',        *archer1.items(), end='\n\n')
print('heavy_soldier1 :', *heavy_soldier1.items(), end='\n\n')
print('heavy_soldier2 :', *heavy_soldier2.items(), end='\n\n')

print('ещё раз наносим 50 единиц урона юниту heavy_soldier1:', end='\n\n')
get_damage(heavy_soldier1, 50)

print('heavy_soldier1 :', *heavy_soldier1.items(), end='\n\n')
