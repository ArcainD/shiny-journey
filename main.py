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
pprint(res)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    print(type(dishes))
    if type(dishes) == str:
        if dishes in res.keys():
            for ingredient in res[dishes]:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': (ingredient['quantity'])*person_count}
            return result
    if type(dishes) == list:
        for dish in dishes:
            for ingredient in res[dish]:
                if ingredient['ingredient_name'] in result.keys():
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
                else:
                    # result[ingredient['ingredient_name']] ={}
                    # result[ingredient['ingredient_name']]['measure'] = ingredient['measure']
                    # result[ingredient['ingredient_name']]['quantity'] = ingredient['quantity']*person_count
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                             'quantity': (ingredient['quantity']) * person_count}
        return result


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 1))
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Омлет'], 5))
pprint(get_shop_list_by_dishes('Омлет', 1))
pprint(get_shop_list_by_dishes('Омлет', 2))




# def print_shop_list(shop_list):
#     for shop_list_item in shop_list.values():
#         print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
#                                 shop_list_item['measure']))
#
#
# def create_shop_list():
#     person_count = int(input('Введите количество человек: '))
#     dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#         .lower().split(', ')
#     shop_list = get_shop_list_by_dishes(dishes, person_count)
#     print_shop_list(shop_list)
#
#
# create_shop_list()



