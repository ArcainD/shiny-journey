from pprint import pprint

with open('cook book.txt', encoding='utf-8') as file:
    res = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp.append(
                {'ingredient_name': ingredient_name.strip(),
                 'quantity': int(quantity.strip()),
                 'measure': measure.strip()}
            )
        res[dish_name] = temp
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    if type(dishes) == str:
        if dishes in res.keys():
            for ingredient in res[dishes]:
                result[ingredient['ingredient_name']] = \
                    {'measure': ingredient['measure'], 'quantity': (ingredient['quantity'])*person_count}
            return result
    if type(dishes) == list:
        for _dish in dishes:
            for ingredient in res[_dish]:
                if ingredient['ingredient_name'] in result.keys():
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
                else:
                    result[ingredient['ingredient_name']] = \
                        {'measure': ingredient['measure'],
                         'quantity': (ingredient['quantity']) * person_count}
        return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))






