from pprint import pprint
import os

path = f'{os.getcwd()}\\recipes.txt'

with open(path, encoding='UTF-8') as file:
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


# def rewrite_file():
#     outout_file = "rewrite_file.txt"
#     with open('1.txt', 'r', encoding='utf-8') as f1:
#         file1 = f1.readlines()
#     with open('2.txt', 'r', encoding='utf-8') as f2:
#         file2 = f2.readlines()
#     with open('3.txt', 'r', encoding='utf-8') as f3:
#         file3 = f3.readlines()
#     with open(outout_file, 'w', encoding='utf-8') as f_total:
#         if len(file1) < len(file2) and len(file1) < len(file3):
#             f_total.write(path1 + '\n')
#             f_total.write(str(len(file1)) + '\n')
#             f_total.writelines(file1)
#             f_total.write('\n')
#         elif len(file2) < len(file1) and len(file2) < len(file3):
#             f_total.write(path2 + '\n')
#             f_total.write(str(len(file2)) + '\n')
#             f_total.writelines(file2)
#             f_total.write('\n')
#         elif len(file3) < len(file1) and len(file3) < len(file2):
#             f_total.write(path3 + '\n')
#             f_total.write(str(len(file3)) + '\n')
#             f_total.writelines(file3)
#             f_total.write('\n')
#         if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(                    file3):
#             f_total.write(path1 + '\n')
#             f_total.write(str(len(file1)) + '\n')
#             f_total.writelines(file1)
#             f_total.write('\n')
#         elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
#                 file3):
#             f_total.write(path2 + '\n')
#             f_total.write(str(len(file2)) + '\n')
#             f_total.writelines(file2)
#             f_total.write('\n')
#         elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
#                 file2):
#             f_total.write(path3 + '\n')
#             f_total.write(str(len(file3)) + '\n')
#             f_total.writelines(file3)
#             f_total.write('\n')
#         if len(file1) > len(file2) and len(file1) > len(file3):
#             f_total.write(path1 + '\n')
#             f_total.write(str(len(file1)) + '\n')
#             f_total.writelines(file1)
#         elif len(file2) > len(file1) and len(file2) > len(file3):
#             f_total.write(path2 + '\n')
#             f_total.write(str(len(file2)) + '\n')
#             f_total.writelines(file2)
#         elif len(file3) > len(file1) and len(file3) > len(file2):
#             f_total.write(path3 + '\n')
#             f_total.write(str(len(file3)) + '\n')
#             f_total.writelines(file3)
#         else:
#             print('hi')
#     return
