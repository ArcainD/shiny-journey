from pprint import pprint

with open('cook book.txt', encoding='utf-8') as file:
    res = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp.append({'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})
        res[dish_name] = temp
        file.readline()
pprint(res)


# def get_shop_list_by_dishes(dishes):
     # result ={}
     # for dish in res.keys():
     #     return dish
#          if dish == dishes:
#              return dish.values()
# print(get_shop_list_by_dishes('Омлет'))
# print(get_shop_list_by_dishes('Омлет'))

