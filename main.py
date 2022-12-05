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
    ingr_list = dict()

    for dish_name in dishes: 
        if dish_name in cook_book:
            for ings in cook_book[dish_name]: 
                meas_quan_list = dict()
                if ings['name'] not in ingr_list:
                    meas_quan_list['unit'] = ings['unit']
                    meas_quan_list['count'] = int(ings['count']) * person_count
                    ingr_list[ings['name']] = meas_quan_list
                else:
                    ingr_list[ings['name']]['count'] = ingr_list[ings['name']]['count'] + int(ings['count']) * person_count

        else:
            print("Такого блюда нет в списке!")
    return ingr_list


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5))
        
# print(cook_book['Омлет'])

