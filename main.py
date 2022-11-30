cook_book = {}
with open('Cook.txt', 'rt', encoding='utf-8') as Cook_data:

    for line in Cook_data:
        dish_name = line.split()
        ingredients_count = int(Cook_data.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingr = Cook_data.readline().strip().split(' | ')
            name, count, unit = ingr
            ingredients.append({'name': name,
                                'count': count,  
                                'unit': unit})
        Cook_data.readline()
        c_b = {
            dish_name[0]: ingredients
        }            
        cook_book.update(c_b)   

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingredients in cook_book[dish_name]:
                ing_name_list = dict()
                if shop_list['name'] not in shop_list:
                    ing_name_list['unit'] = ingredients['unit']
                    ing_name_list['count'] = ingredients['count'] * person_count
                    shop_list[ingredients['name']] = ing_name_list
                else:
                    shop_list[ingredients['name']]['count'] = shop_list[ingredients['name']]['count'] + ingredients['count'] * person_count
        else: print(f'\n"Такого блюда нету в книге("\n')
    return shop_list


print(get_shop_list_by_dishes('Фахитос', 3))
        
# print(cook_book['Омлет'])