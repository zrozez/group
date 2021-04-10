group = {
    'partic1':{'name': 'Elya', 'age': 21, 'role': 'singer'},
    'partic2':{'name':'Sezya', 'age':20, 'role':'dancer'},
    'partic3':{'name':'Nuriza', 'age':22, 'role':'leader'}}

#Функция добавления участника в группу
def add_participant (number_of_partic, name, age, role, group):
    prof = number_of_partic
    number_of_partic = {}
    number_of_partic['name'] = name
    number_of_partic['age'] = age
    number_of_partic['role'] = role
    group[prof] = number_of_partic
    return group
#проверим работает ли
print(add_participant('partic4', 'Roze', 20, 'dancer', group))

#Функция исключения участника из группы
def del_participant (number_of_partic, group):
    del group[number_of_partic]
    return group
#проверим работоспособность функции
print(del_participant('partic1', group))

#отправим группу на концерт
from datetime import date
concert = {
    'NewYork':{'contract': 10000, 'food': 500, 'hotel': 1000, 'ticket': 400, 'date': date(2021, 8, 21)},
    'London':{'contract': 12000, 'food':600, 'hotel':900, 'ticket': 400, 'date': date(2021, 8, 23)},
    'Astana':{'contract': 8000, 'food':400, 'hotel': 700, 'ticket': 100, 'date': date(2021, 8, 26)},
    'Tashkent':{'contract': 8000, 'food':300, 'hotel': 600, 'ticket': 200, 'date': date(2021, 8, 28)},
    'Bishkek':{'contract':6000, 'food':200, 'hotel': 200, 'ticket': 50, 'date': date(2021, 8, 31)}}
print(concert['NewYork']['date']) #проверили работу datetime

#Функция добавления концерта в группу
def add_concert (city, contract, food, hotel, ticket, date, concert):
    city1 = city
    city = {}
    city['contract'] = contract
    city['food'] = food
    city['hotel'] = hotel
    city['ticket'] = ticket
    city['date'] = date
    concert[city1] = city
    return concert
#Проверим работу функции
print(add_concert('Ottawa', 7000, 350, 600, 300, date(2021, 8, 20), concert))

#Функция подсчета затрат по городу
def sum_zatraty(city, concert):
    summa_zatrat = concert[city]['food'] + concert[city]['hotel'] + concert[city]['ticket']
    return summa_zatrat

#функция подсчета дохода
def itogo_pr (city, function_of_zatraty, concert):
    contract = concert[city]['contract']
    zatraty = function_of_zatraty(city, concert)
    return contract - zatraty
#подсчитаем итого прибыли используя нашу функцию
itogo_pribyly = 0
for city in concert:
    ii = itogo_pr(city, sum_zatraty, concert)
    itogo_pribyly += ii
print(itogo_pribyly)