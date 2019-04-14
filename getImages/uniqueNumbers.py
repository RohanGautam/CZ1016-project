import json

uniqAttack, uniqCost, uniqHealth=[], [], []

with open('cards.json') as f:
    data=json.load(f)
    for card in data:
        if ('attack' in card.keys()) and (card['attack'] not in uniqAttack):
            uniqAttack.append(card['attack'])
        if ('cost' in card.keys()) and (card['cost'] not in uniqCost):
            uniqCost.append(card['cost'])
        if ('health' in card.keys()) and (card['health'] not in uniqHealth):
            uniqHealth.append(card['health'])

uniqAttack, uniqCost, uniqHealth=sorted(uniqAttack), sorted(uniqCost), sorted(uniqHealth)

print(uniqAttack)
print(uniqCost)
print(uniqHealth)

print(sorted(list(set(uniqAttack+uniqCost+uniqHealth))))

'''
a-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
c-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 50]
h-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 40, 45, 50, 55, 60, 70, 75, 80, 85, 95, 99, 100, 200, 400, 1000]

a+c+h-[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 35, 40, 45, 50, 55, 60, 70, 75, 80, 85, 95, 99, 100, 200, 400, 1000]
'''