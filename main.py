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
    shop_list = {}
    if dishes == cook_book[0]:
        
    else:
        print('Ошибка')
    
