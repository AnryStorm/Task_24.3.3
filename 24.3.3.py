import requests
import json

pet_1 = 'Бус'
pet_2 = 'Каспер'

data = {
  'id': 0,
  'category': {'id': 0, 'name': 'string'},
  'name': pet_1,
  'photoUrls': ['string'],
  'tags': [{'id': 0, 'name': 'string'}],
  'status': 'available'
}

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Host': 'petstore.swagger.io',
    'Content-Length': '236',
    'Cache-Control': 'no-cache'
}

# POST-запрос
res_1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(res_1.status_code)
print('Код ответа - 200\nПитомец создан\n')

pet_id = dict(res_1.json())['id']

data['id'] = pet_id
data['name'] = pet_2

# PUT-запрос
res_2 = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(res_2.status_code)
print(f'Код ответа - 200\nИмя питомца "{pet_1}" изменено на "{pet_2}"')

print('\nЗапрос с сервера данных о питомце по id - ' + str(pet_id))

# GET-запрос
res_3 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_3.status_code)
print('Код ответа - 200 \nНа сервере имеются данные')

print('\nУдаление данных о питомце по id - ' + str(pet_id))

# DELETE-запрос
res_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_4.status_code)
print('Код ответа - 200 \nС сервера удалены данные о питомце')

print('\nПовторный запрос с сервера данных о питомце по id - ' + str(pet_id))

# Повторный GET-запрос
res_5 = requests.get(f'https://petstore.swagger.io/v2/pet/{pet_id}', headers=headers)

print(res_5.status_code)
print('Код ответа - 404 \nНа сервере нет данных о питомце')