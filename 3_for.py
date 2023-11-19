"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}]
    summ_sold_iphone = 0
    summ_sold_xiaomi = 0
    summ_sold_samsung = 0
    for i in data[0]['items_sold']:
        summ_sold_iphone += i
    for i in data[1]['items_sold']:
        summ_sold_xiaomi += i
    for i in data[2]['items_sold']:
        summ_sold_samsung += i

    print(f'суммарное количество продаж для {data[0]["product"]}: {summ_sold_iphone}')
    print(f'суммарное количество продаж для {data[1]["product"]}: {summ_sold_xiaomi}')
    print(f'суммарное количество продаж для {data[2]["product"]}: {summ_sold_samsung}')
    print()

    avg_summ_sold_iphone = summ_sold_iphone / len(data[0]['items_sold'])
    avg_summ_sold_xiaomi = summ_sold_iphone / len(data[1]['items_sold'])
    avg_summ_sold_samsung = summ_sold_iphone / len(data[2]['items_sold'])

    print(f'среднее количество продаж для {data[0]["product"]}: {avg_summ_sold_iphone}')
    print(f'среднее количество продаж для {data[1]["product"]}: {avg_summ_sold_xiaomi}')
    print(f'среднее количество продаж для {data[2]["product"]}: {avg_summ_sold_samsung}')
    print()

    summ_sold_products = summ_sold_iphone + summ_sold_xiaomi + summ_sold_samsung
    print(f'суммарное количество продаж всех товаров: {summ_sold_products}')
    print()

    avg_summ_sold_products = summ_sold_products / (len(data[0]['items_sold']) + len(data[1]['items_sold']) + len(data[2]['items_sold']))
    print(f'среднее количество продаж всех товаров: {avg_summ_sold_products}')

if __name__ == "__main__":
    main()
