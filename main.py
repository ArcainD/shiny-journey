from pprint import pprint

with open('cook book.txt', encoding='utf-8') as file:
    res = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        res[dish] = temp
        file.readline()
    pprint(res)
