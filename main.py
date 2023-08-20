# from tkinter import *
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_rectangle(100,100,120,120,fill='orange', outline='orange')
# canvas.create_rectangle(140,140,180,180,fill='blue', outline='blue')
# canvas.create_rectangle(200,200,260,260,fill='green', outline='green')
# window.mainloop()

# from tkinter import *
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_polygon(10, 260, 60, 200, 110, 260, fill='green', outline='black')
# canvas.create_rectangle(20, 260, 100, 360, fill='red', outline='black')
# canvas.create_rectangle(45, 290, 75, 320, fill='blue', outline='black')
# canvas.create_rectangle(1, 2000, 1100, 360, fill='DarkOrange4', outline='black')
# canvas.create_oval(650, 80, 720, 10, fill='yellow', outline='yellow')
# window.mainloop()

# import random
# import telebot
#
# token = '6017975055:AAFsSV0K97nkcgelXzgAcy0ovKyD7BTB1w8'
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     welcome_text = 'Здарова! Этот бот для всех тех, кто шарит за медведей!'
#     bot.send_message(message.chat.id, welcome_text)
#
# @bot.message_handler(commands=['photo'])
# def send_medvedi(message):
#     medvedi_number = str(random.randint(1, 8))
#     medvedi_img = open('img/' + medvedi_number + '.jpg', 'rb')
#     bot.send_photo(message.chat.id, medvedi_img)
#
#
# bot.polling()
# print()
# print('Формула Дискриминанта: D = b**2 - 4 * a * c ')
# print()
# a = int(input('Введите число A: '))
# b = int(input('Введите число B: '))
# c = int(input('Введите число C: '))
# D = b**2 - 4 * a * c
# if D<0:
#     print('Корней нет')
# print()
# print('Дискриминант =', D)
# print()
# print('Формула x_1: x_1 = -b - √D / 2a')
# print()
# print('Формула x_2: x_2 = -b + √D / 2a')
# print()
# x_1 = -b-D**0.5/2*a
# x_2 = -b+D**0.5/2*a
# print('x_1 =', x_1)
# print()
# print('x_2 =', x_2)
# print()

# from tkinter import *
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_rectangle(50, 50, 70, 70, fill='white', outline='orange')
# canvas.create_rectangle(80, 65, 120, 105, fill='white', outline='blue')
# canvas.create_rectangle(130, 90, 190, 150, fill='white', outline='green')
# window.mainloop()

# from tkinter import *
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# canvas.create_rectangle(250, 250, 400, 400, fill='green', outline='')
# canvas.create_polygon(250,250,325,150,400,250, fill='red', outline='')
# canvas.create_rectangle(310, 340, 340, 400, fill='yellow', outline='')
# canvas.create_rectangle(270, 280, 310, 320, fill='blue', outline='')
# canvas.create_rectangle(340, 280, 380, 320, fill='blue', outline='')
# canvas.create_rectangle(0, 400, 800, 600, fill='purple', outline='')
# window.mainloop()

# class User:
#     def __init__(self, health, damage):
#         self.health = health
#         self.damage = damage
#     def print_damage(self):
#         print()
#         if a == 1:
#             print('Я наношу', self.damage, 'урон!', 'Осталось', self.health, 'здоровья.')
#         else:
#             print('Я наношу', self.damage, 'урона!', 'Осталось', self.health, 'здоровья.')
# print()
# a = int(input('Введите количество урона: '))
# user1 = User('100', a)
# user1.print_damage()

# from tkinter import *
# window = Tk()
# window.geometry('800x600')
# canvas = Canvas(window, width=800, height=600, bg='white')
# canvas.pack()
# class House:
#     def __init__(self, x, y, height, width):
#         self.x = x
#         self.y = y
#         self.height = height
#         self.width = width
#     def draw_house(self):
#         canvas.create_rectangle(self.x, self.y, self.width, self.height, fill='red', outline='black')
# user1 = House(250,250,400,400)
# user1.draw_house()
# class House:
#     def __init__(self, x2, y2, height2, width2, x3, y3):
#         self.x2 = x2
#         self.y2 = y2
#         self.height2 = height2
#         self.width2 = width2
#         self.x3 = x3
#         self.y3 = y3
#     def draw_house(self):
#         canvas.create_polygon(self.x2, self.y2, self.width2, self.height2, self.x3, self.y3, fill='green', outline='black')
# user2 = House(325,180,250,200,450,250)
# user2.draw_house()
# class House:
#     def __init__(self, x4, y4, height3, width3):
#         self.x4 = x4
#         self.y4 = y4
#         self.height3 = height3
#         self.width3 = width3
#     def draw_house(self):
#         canvas.create_rectangle(self.x4, self.y4, self.width3, self.height3, fill='blue', outline='black')
# user3 = House(300,320,290,270)
# user3.draw_house()
# class House:
#     def __init__(self, x5, y5, height4, width4):
#         self.x5 = x5
#         self.y5 = y5
#         self.height4 = height4
#         self.width4 = width4
#     def draw_house(self):
#         canvas.create_rectangle(self.x5, self.y5, self.width4, self.height4, fill='blue', outline='black')
# user4 = House(350,320,290,380)
# user4.draw_house()
# window.mainloop()






#
# from tkinter import *
# import random
# window = Tk()
# w = 1024
# h = 923
# window.geometry(str(w) + 'x' + str(h))
# canvas = Canvas(window, width=w, height=h)
# canvas.pack()
# bg_photo = PhotoImage(file='castle33.png')
# class Knight:
#     def __init__(self):
#         self.x = 85
#         self.y = h//2
#         self.v = 0
#         self.vx = 0
#         self.photo = PhotoImage(file='knight.png')
#     def up(self, event):
#         self.v = -3
#     def down(self, event):
#         self.v = 3
#     def right(self, event):
#         self.vx = 3
#     def left(self, event):
#         self.vx = -3
#     def stop(self, event):
#         self.v = 0
# class Dragon:
#     def __init__(self):
#         self.x = 1150
#         self.y = random.randint(100, 500)
#         self.v = 3
#         self.photo = PhotoImage(file='dragon2.png')
# knight = Knight()
# dragons = []
# for i in range(3):
#     dragons.append(Dragon())
# def game():
#     canvas.delete('all')
#     canvas.create_image(512, 461, image=bg_photo)
#     canvas.create_image(knight.x, knight.y, image=knight.photo)
#
#     if knight.y >= 0 and knight.y <= 923:
#         knight.y += knight.v
#     else:
#         knight.v = 0
#
#     if knight.x >= 0 and knight.x <= 1024:
#         knight.x += knight.vx
#     else:
#         knight.vx = 0
#
#     current_dragon = 0
#     dragon_to_kill = -1
#     for dragon in dragons:
#         dragon.x -= dragon.v
#         canvas.create_image(dragon.x, dragon.y, image=dragon.photo)
#         if ((dragon.x-knight.x)**2) + ((dragon.y-knight.y)**2) <= (96)**2:
#             dragon_to_kill = current_dragon
#         current_dragon += 1
#         if dragon.x <= 0:
#             canvas.delete('all')
#             canvas.create_text(w//2, h//2, text='You lose!', font='Verdana 42', fill='red')
#             break
#     if dragon_to_kill >= 0:
#         del dragons[dragon_to_kill]
#     if len(dragons) == 0:
#         canvas.delete('all')
#         canvas.create_text(w // 2, h // 2, text='You win!', font='Verdana 42', fill='red')
#     else:
#         window.after(5, game)
# game()
# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<Key-Right>', knight.right)
# window.bind('<Key-Left>', knight.left)
# window.bind('<KeyRelease>', knight.stop)
# window.mainloop()









#
# import requests
# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# people_api = response['people']
# planets_api = response['planets']
# starships_api = response['starships']
# def check_people(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['height'])
#
# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['diameter'])
#
# def check_starships(url):
#     for i in range(2, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['max_atmosphering_speed'])
# check_people(people_api)
# check_planets(planets_api)
# check_starships(starships_api)



#
# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
# day = input('Введите день (Например 01): ')
# month = input('Введите месяц (Например 01): ')
# year = input('Введите год (Например 2021): ')
# url = url + day + '/' + month + '/' + year
# response = requests.get(url).content
# xml = BeautifulSoup(response, 'lxml')
# id = input('Введиту id валюты (R01235 - USD, R01335 - KTG, R01239 - EUR) ')
# res = xml.find('valute', {'id': id})
# print('Курс на ' + day + '.' + month + '.' + year)
# print(res.charcode.text + ':' + res.value.text)



# import random
# class Tank:
#     def __init__(self, model, health, armor, min_damage, max_damage):
#         self.model = model
#         self.health = health
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
#     def print_info(self):
#         print(f'{self.model} имеет {self.health} хп и {self.damage} урона')
#     def health_down(self, damage):
#         print('\n')
#         self.health = self.health - damage
#         print(f'[{self.model}]: Командир, по нашему экипажу {self.model} попали, у нас осталось {self.health} хп')
#     def shot(self, enemy):
#         if enemy.health <= 0 or self.damage >= enemy.health:
#             enemy.health = 0
#             print(f'[{self.model}]: {enemy.model} уничтожен')
#         else:
#             enemy.health_down(self.damage)
#             print(f'[{self.model}]: Точно в цель! Теперь у противника {enemy.model} {enemy.health} хп')
# tank1 = Tank('Т-34', 200, 100, 50, 100)
# tank2 = Tank('Mouse', 150, 80, 10, 80)
# tank1.print_info()
# tank2.print_info()
# tank1.shot(tank2)
# tank2.shot(tank1)
# tank1.shot(tank2)
# tank2.shot(tank1)



# import random
# class User:
#     def __init__(self, character, health, min_damage, max_damage):
#         self.character = character
#         self.health = health
#         self.damage = random.randint(min_damage, max_damage)
# class Mag(User):
#     def print_damage(self):
#         print(self.character, ':', 'Я отравляю и наношу', self.damage, 'урона!', 'У меня осталось', self.health, 'здоровья.')
# class Voin(User):
#     def print_damage(self):
#         print(self.character, ':', 'Я дерусь и наношу', self.damage, 'урона!', 'У меня осталось', self.health, 'здоровья.')
# class Luchnik(User):
#     def print_damage(self):
#         print(self.character, ':', 'Я стреляю и наношу', self.damage, 'урона!', 'У меня осталось', self.health, 'здоровья.')
# mag = Mag('Skywrath', 150, 50, 100)
# voin = Voin('Pudje', 200, 80, 100)
# luchnik = Luchnik('Skelet', 100, 50, 80)
# mag.print_damage()
# voin.print_damage()
# luchnik.print_damage()

# class Employee:
#     def __init__(self, name, salary, on_vacation):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#     def get_info(self):
#         print(f'У {self.name} зарплата в месяц {self.salary} рублей. В отпуске? - {self.on_vacation}')
# employee_list = [Employee('Даниил', 200_000, 'Да'), Employee('Олег', 150_000, 'Нет'), Employee('Никита', 180_000, 'Нет')]
# for employee in employee_list:
#     employee.get_info()





# class Employee:
#     def __init__(self, name, salary, on_vacation, is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = on_vacation
#         self.is_good_employee = is_good_employee
#     def get_info(self):
#         print(f'У {self.name} зарплата в месяц {self.salary} рублей. В отпуске? - {self.on_vacation}. Сотрудник хороший? - {self.is_good_employee}')
# employee_list = [Employee('Даниил', 200_000, 'Да', True), Employee('Олег', 150_000, 'Нет', True), Employee('Никита', 180_000, 'Нет', False), Employee('Артём', 250_000, 'Нет', True), Employee('Иван', 120_000, 'Да', True)]
# for employee in employee_list:
#     if employee['is_good_employee'] == False:
#         employee_list.remove(employee)
#         print('***Сотрудник уволен***')
#         break
#     employee.get_info()










#
# import vk_api
# token = 'vk1.a.yppM8qdZmlyrXFxJLoWjTcp1rnZd2YIOZaV73oWgnyZd78DXSItoV4SV3U8dJ_0PR_pd52EQzXjmgyPOKy4b2B9xLa-qLe6f-OeVEiHW6tMI6x4KRT3E3wnfJTWBgWEsMR4KdBxxY52W-PMCEDfIsaLwTpTodDZwb6FhWNuXvqIf8L91FBGKiAOEtDPEt4kIFs-x87Qb6pvP79pC5v40Lg'
# vk_session = vk_api.VkApi(token=token)
# vk = vk_session.get_api()
# while True:
#    messages = vk.messages.getConversations(count=20, filter='unanswered')
#    if messages['count'] >= 1:
#        message_text = messages['items'][0]['last_message']['text']
#        user_id = messages['items'][0]['last_message']['from_id']
#        message_id = messages['items'][0]['last_message']['random_id']
#        if message_text.lower() == 'планеты':
#            import requests
#            url = 'https://swapi.dev/api/'
#            response = requests.get(url).json()
#            planets_api = response['planets']
#            def check_planets(url):
#                for i in range(1, 6):
#                    response = requests.get(url + str(i)).json()
#                    print('Название планеты:', response['name'], '         Её диаметр:', response['diameter'])
#            vk.messages.send(user_id=user_id, random_id=message_id, message=check_planets(planets_api))

# import vk_api
# token = 'vk1.a.yppM8qdZmlyrXFxJLoWjTcp1rnZd2YIOZaV73oWgnyZd78DXSItoV4SV3U8dJ_0PR_pd52EQzXjmgyPOKy4b2B9xLa-qLe6f-OeVEiHW6tMI6x4KRT3E3wnfJTWBgWEsMR4KdBxxY52W-PMCEDfIsaLwTpTodDZwb6FhWNuXvqIf8L91FBGKiAOEtDPEt4kIFs-x87Qb6pvP79pC5v40Lg'
# vk_session = vk_api.VkApi(token=token)
# vk = vk_session.get_api()
# while True:
#    messages = vk.messages.getConversations(count=20, filter='unanswered')
#    if messages['count'] >= 1:
#        message_text = messages['items'][0]['last_message']['text']
#        user_id = messages['items'][0]['last_message']['from_id']
#        message_id = messages['items'][0]['last_message']['random_id']
#        if message_text.lower() == 'корабли':
#            import requests
#            url = 'https://swapi.dev/api/'
#            response = requests.get(url).json()
#            starships_api = response['starships']
#            def check_starships(url):
#                for i in range(2, 6):
#                    response = requests.get(url + str(i)).json()
#                    print('Название корабля:', response['name'], '         Его максимальная скорость:', response['max_atmosphering_speed'])
#            vk.messages.send(user_id=user_id, random_id=message_id, message=check_starships(starships_api))
#
# import requests
# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# people_api = response['people']
# planets_api = response['planets']
# starships_api = response['starships']
# def check_people(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['height'])
#
# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['diameter'])
#
# def check_starships(url):
#     for i in range(2, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['name'], response['max_atmosphering_speed'])
# check_people(people_api)
# check_planets(planets_api)
# check_starships(starships_api)

# import requests
# url = 'https://swapi.dev/api/'
# response = requests.get(url).json()
# planets_api = response['planets']
# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(url + str(i)).json()
#         print(response['diameter'])
#         check_planets(planets_api)
# my_list = [str(check_planets(planets_api))]
# print(my_list)
# max_value = max(my_list)
# print(max_value)


# print(messages['items'])
# print(messages['items'][0])
# print(messages['items'][0]['last_message'])
# print(messages['items'][0]['last_message']['text'])


# import vk_api
# from vk_api.longpoll import VkLongPoll
# token = 'vk1.a.yppM8qdZmlyrXFxJLoWjTcp1rnZd2YIOZaV73oWgnyZd78DXSItoV4SV3U8dJ_0PR_pd52EQzXjmgyPOKy4b2B9xLa-qLe6f-OeVEiHW6tMI6x4KRT3E3wnfJTWBgWEsMR4KdBxxY52W-PMCEDfIsaLwTpTodDZwb6FhWNuXvqIf8L91FBGKiAOEtDPEt4kIFs-x87Qb6pvP79pC5v40Lg'
# vk_session = vk_api.VkApi(token=token)
# vk = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)
# for event in longpoll.listen():
#     if event.type == 4 and event.to_me:
#         text = event.text
#         user_id = event.user_id
#         message_id = event.message_id
#         if text.lower() == 'привет':
#             vk.messages.send(user_id=user_id, random_id=message_id, message='Здарова брат!!!')
#         else:
#             vk.messages.send(user_id=user_id, random_id=message_id, message='Я тебя не понимаю')

# def generator():
#     for x in range(1_000_001):
#         print('До:', x)
#         print('Возведём в квадрат, получим: ')
#         yield x**2
#         print()
# for i in generator():
#     print(i)
#
#
# generator = (x for x in range(0, 1_000_001))
# for elem in generator:
#     print('До:', elem)
#     x = elem**2
#     print('Возведём в квадрат, получим: ', x)
#     print()




# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
# day = input('Введите день (Например 01): ')
# month = input('Введите месяц (Например 01): ')
# year = input('Введите год (Например 2021): ')
# url = url + day + '/' + month + '/' + year
# response = requests.get(url).content
# xml = BeautifulSoup(response, 'lxml')
# id = input('Введиту id валюты (R01235 - USD, R01335 - KTG, R01239 - EUR) ')
# res = xml.find('valute', {'id': id})
# print('Курс на ' + day + '.' + month + '.' + year)
# print(res.charcode.text + ':' + res.value.text)



# class MyFile:
#     def __init__(self, name, mode):
#         self.name = name
#         self.mode = mode
#     def __enter__(self):
#         self.file = open(self.name, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()


# class Iterator:
#     def __init__(self, start):
#         self.start = start
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start += 1
#         return self.start - 1



# class Year:
#     def __init__(self, days):
#         self.days = days
#
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Некорректное значение')
#
# year = Year(365)
#
# year.days = 360
#
# print(year.days)




# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age(self):
#         if (self.name == None):
#             return "Member not found"
#         return str(self.name) + '-' + str(self.age)
#
#     @age.setter
#     def age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             raise Exception('Вы ещё не родились')
#
#     @age.deleter
#     def age(self):
#         self.name = None
#         self.age = None
#
# person = Person('Иван', 25)
#
# print(person.age)
#
# del person.age
#
# print(person.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def characteristics(self):
#         if (self.name == None):
#             return 'Такого человека не найдено'
#         return str(self.name) + ' - ' + str(self.age) + ' лет'
#
#     @characteristics.setter
#     def email(self, clg_characteristics):
#         name = clg_characteristics
#         self.name = name
#
#     @characteristics.deleter
#     def email(self):
#         self.name = None
#         self.age = None
#
#
# person = Person('Иван', 25)
# print(person.characteristics)
#
# del person.email
# print('Удаление сведений.....')
# print(person.characteristics)






# class Item:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other
#
#     def __sub__(self, other):
#         if isinstance(other, Item):
#             return self.price - other.price
#         elif isinstance(other, int):
#             return self.price - other
#
#     def __mul__(self, other):
#         if isinstance(other, Item):
#             return self.price * other.price
#         elif isinstance(other, int):
#             return self.price * other
#
#     def __floordiv__(self, other):
#         if isinstance(other, Item):
#             return self.price // other.price
#         elif isinstance(other, int):
#             return self.price // other
#
# item1 = Item('Процессор i5 12400f', 15000)
# item2 = Item('Видеокарта 1660s', 20000)
#
# print(item1 + item2)
# print(item2 - item1)
# print(item1 * item2)
# print(item1 // item2)




# from tkinter import *
# import random
#
# window = Tk()
# window.geometry('600x600')
#
# class Fire:
#     image = PhotoImage(file='elements/fire.png').subsample(16, 16)
#     def __add__(self, other):
#         if isinstance(other, Ground):
#             return Clay
#
# class Water:
#     image = PhotoImage(file='elements/water.png').subsample(5, 5)
#     def __add__(self, other):
#         if isinstance(other, Ground):
#             return Mud
#
# class Ground:
#     image = PhotoImage(file='elements/ground.png').subsample(5, 5)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
#         elif isinstance(other, Wind):
#             return Dust
#         elif isinstance(other, Water):
#             return Mud
#
# class Wind:
#     image = PhotoImage(file='elements/wind.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Ground):
#             return Dust
#
# class Clay:
#     image = PhotoImage(file='elements/clay.png').subsample(4, 4)
#
# class Mud:
#     image = PhotoImage(file='elements/mud.png').subsample(4, 4)
#
# class Dust:
#     image = PhotoImage(file='elements/Dust.png').subsample(4, 4)
#
# canvas = Canvas(window, width=600, height=600)
# canvas.pack()
#
# elements = [Fire(), Ground(), Water(), Wind()]
#
# for elem in elements:
#     img = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)
#
# def move(event):
#     images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
#     canvas.coords(images_id, event.x, event.y)
#     if len(images_id) == 2:
#         element1 = elements[images_id[0]-1]
#         element2 = elements[images_id[1] - 1]
#         new_element = element1+element2
#         if new_element not in elements:
#             canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=new_element.image)
#             elements.append(new_element)
#
# window.bind('<B1-Motion>', move)
#
# window.mainloop()



#
# class Item:
#
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return self.brand
#
# items_list = [
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, 'Samsung'),
#     Item(660, 'Xiaomi'),
# ]
#
# result = filter(lambda item: item['brand'] == 'Apple', items_list)
#
# print(list(result))






# names_list = ['данил', 'артём', 'никита', 'влад']
# names_map = map(lambda item: item.capitalize(), names_list)
# print(list(names_map))





# import sqlite3
# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
# def create_table_users(data_base):
#     command = """
#         CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         surname TEXT,
#         gender TEXT
#         );
#     """
#     data_base.execute(command)
# def add_user(data_base, user):
#     command = """
#          INSERT INTO users(name, surname, gender)
#          VALUES(?, ?, ?)
#     """
#     data_base.execute(command, (user.name, user.surname, user.gender))
# def get_users_list():
#     command = """
#         SELECT * FROM Users
#     """
#     result = data_base.execute(command)
#     print(list(result))
# def delete_users(data_base):
#     command = """
#         DELETE FROM users
#     """
#     data_base.execute(command)
# with sqlite3.connect('data.db') as data_base:
#     create_table_users(data_base)
#     add_user(data_base, User('Иван', 'Иванов', 'Мужчина'))
#     get_users_list()
#     delete_users(data_base)
#     get_users_list()






1   1   !!1     111 !!!!    1



































































































































































































































































































































