```
from time import sleep
import requests
import fake_useragent
from bs4 import BeautifulSoup
import json
import csv

ua = fake_useragent.UserAgent()

headers = {'User-Agent': ua.random, "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"}
#
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
#
# # save page in file
# with open('./data/index.html', 'w') as file:
#     file.write(src)

# # call page
# with open('./data/index.html') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#
#     all_categories_dict[item_text] = item_href
#
# # save dict to json
# with open('./data/all_categories_dict.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('./data/all_categories_dict.json') as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f'Всего итераций: {iteration_count}')

for category_name, category_href in all_categories.items():


    rep = [',', ' ', '-']
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f'./data/{count}_{category_name}.html', 'w')as file:
        file.write(src)
    with open(f'./data/{count}_{category_name}.html')as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # Проверка страницы на наличие таблицы
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    #  данные заголовка таблицы

    table_head = soup.find(class_='mzr-tc-group-table').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    protein = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f'./data/{count}_{category_name}.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((
            product,
            calories,
            protein,
            fats,
            carbohydrates

        ))

    # Данные продуктов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    product_info = []
    for item in products_data:
        product_tds = item.find_all('td')

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        protein = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        product_info.append(
            {
                'Title': title,
                'Calories': calories,
                'Protein': protein,
                'Fats': fats,
                'Carbohydrates': carbohydrates

            }
        )

        with open(f'./data/{count}_{category_name}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow((
                title,
                calories,
                protein,
                fats,
                carbohydrates
            ))

    with open(f'./data/{count}_{category_name}.json', 'a', encoding='utf-8') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f'# Итерация {count}. {category_name} записан...')
    iteration_count = iteration_count - 1

    if iteration_count == 0:
        print('Работа завершина')
        break

    print(f'Осталось итераций: {iteration_count}')
    sleep(2)






```
