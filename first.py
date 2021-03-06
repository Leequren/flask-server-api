import requests
from bs4 import BeautifulSoup as bs
import json


def Get_parse(ssilka):
    response = requests.get(ssilka)  # Не забыть сделать привязку по ссылке

    htmlka = bs(response.content, 'html.parser')
    headers = list()
    customers = list()
    purchase_objects = list()
    registary_numbers = list()
    list_of_status = list()
    list_of_start_values = list()

    for header in htmlka.select(".registry-entry__header-top__title"):  # Парсим хэдеры
        headers.append(str(' '.join(str(header).split(">")[1].split("<")[0].split())))

    for purchase in htmlka.select(".registry-entry__body-value"):  # Парсим объект закупки
        purchase_objects.append(str(purchase).split(">")[1].split("<")[0])

    for customer in htmlka.select(".registry-entry__body-href"):  # Добавление заказчиков
        customers.append(str(' '.join(str(customer).split("<")[2].split()[3:])))

    for registary_number in htmlka.select(".registry-entry__header-mid__number"):
        registary_numbers.append(str(' '.join(str(registary_number).split("<")[2].split()[-2:])))

    for status in htmlka.select(".registry-entry__header-mid__title"):
        list_of_status.append(str(' '.join(str(status).split("<")[1].split()[-2:])))

    for value in htmlka.select(".price-block__value"):
        list_of_start_values.append(str(''.join(str(value).split("<")[1].split()[1:]).split(">")[1]))

    d = dict()
    list_of_all = list()  # В этом списке будут лежать все данные в ввиде json
    n = len(customers)  # Берём длинну всех блоков на сайте
    for i in range(n):
        list_of_all.append({"head": headers[i], "customer": customers[i], "purchase_object": purchase_objects[i],
                            "registary_number": registary_numbers[i],
                            "status": list_of_status[i], "start_value": list_of_start_values[i]})
    d["answer"] = list_of_all
    return json.dumps(d, ensure_ascii=False)

