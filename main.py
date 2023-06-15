import json

with open('task1.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    cook_book = {}
    for i in f:
        name_dish = []
        ingredient_count = int(f.readline())
    for a in ingredient_count.strip().split('|'):
        ingredient_list = {}
        ingredient_name, quantity, measure = f.readline().strip().split(' | ')
        ingredient_list.append({
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure,
        })
        f.readline()
        cook_book[i.strip()] = ingredient_list
    res = json.dumps(cook_book, indent=2)
    print(res)



