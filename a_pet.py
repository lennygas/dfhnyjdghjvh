import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bs4 import BeautifulSoup
import requests
import datetime
import json
import random

class Server:

	def __init__(self, api_token, group_id, server_name: str="Empty"):

		# Даем серверу имя
		self.server_name = server_name

		self.group_id = group_id

		# Для Long Poll
		self.vk = vk_api.VkApi(token=api_token)
		
		# Для использования Long Poll API
		self.long_poll = VkBotLongPoll(self.vk, group_id, wait=30)
		
		# Для вызова методов vk_api
		self.vk_api = self.vk.get_api()

		self.users = {}

		print("Сервер - " + self.server_name + " загружен и готов к работе")

	def send_msg(self, send_id, message):
		"""
		Отправка сообщения через метод messages.send
		:send_id: vk id пользователя, который получит сообщение
		:random_id: id сообщения
		:message: содержимое отправляемого письма
		:return: None
		"""
		self.vk_api.messages.send(peer_id=send_id,
								  random_id=0,
								  message=message)

	def start(self):
		for event in self.long_poll.listen():

			filename = "bd.txt"
			day = datetime.datetime.today().isoweekday()
			a3 = datetime.datetime.today().date()
			if day == 7:
				a1 = []
				ofile = open(filename, 'r+')
				if a3.day % 2 == 0:
					a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=1')
				elif a3.day % 2 != 0:
					a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=0')
				json.dump(a1, ofile)
				ofile.close()
			ofile = open(filename, 'r')
			json_data = json.load(ofile)
			html = requests.get(json_data[0]).text
			soup = BeautifulSoup(html, 'lxml')
			ofile.close()

			rtime = datetime.datetime.today().time()
			times = datetime.time(7)

			que = ['может сразу на завод пойдешь?', 'у меня нет слов, одни междометия', 'пожалуй, я промолчу', 'ну тут только в окно']
			iqseventyn = ['Не удивительно, что ты учишься в АПЭТ', 'Ну, бывает и хуже', 'Хотя бы не в минус', 'Странно, что ты вообще можешь связать речь..', 'IQ не зубы, еще вырастет']
			iqninty = ['Удивлен, что ты до сих пор учишься тут', 'Рад, что ты лучше некоторых', 'Даже у меня меньше', 'Для завода достаточно']
			iqsuper = ['Это что, Илон Маск?', 'Почему ты до сих пор живешь на Земле?', 'Ты вообще с этой планеты?']

			bydn = "Расписание звонков в будни\n1 пара: 08:30-10:00\n2 пара: 10:10-11:40\n3 пара: 12:20-13:40\n4 пара: 13:50-15:10"
			subb = "Расписание звонков в субботу\n1 пара: 08:30-09:40\n2 пара: 09:50-11:00\n3 пара: 11:10-12:20\n4 пара: 12:30-13:40"

			daus = {'!расп понедельник': 1, '!расп вторник': 2, '!расп среда': 3, '!расп четверг': 4, '!расп пятница': 5, '!расп суббота': 6}


			if event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "стогова":
				self.send_message(event.object.peer_id, 'Обнаружена Стогова, блятб, иди нахуй')

			elif event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "!расп":
				if day <= 6 and rtime < times:
					if day == 6:
						self.send_message(event.object.peer_id, subb)
					else:
						self.send_message(event.object.peer_id, bydn)
					for tr in soup.find_all('tr', at_col = 't' + str(day)):
						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

						if zan == None:
							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
						else:
							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 7:
					self.send_message(event.object.peer_id, bydn)
					for tr in soup.find_all('tr', at_col = 't1'):
						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

						if zan == None:
							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
						else:
							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				else:
					if day == 5 and rtime > times:
						self.send_message(event.object.peer_id, subb)
					else:
						self.send_message(event.object.peer_id, bydn)
					for tr in soup.find_all('tr', at_col = 't' + str(day + 1)):
						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

						if zan == None:
							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
						else:
							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')
					

			elif event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() in daus:
				self.send_message(event.object.peer_id, bydn)
				for tr in soup.find_all('tr', at_col = 't' + str(daus[event.object.text])):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')


			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!iq" or event.object.text == "!айку":
				username = self.get_user_name(event.object.from_id)
				podkr = ['Ну это просто бог какой-то', 'Произошла подкрутка', 'Пиздец, мой создатель дебил и крутит очки айку для своей герлфренд и себя']

				iq = random.randint(1, 150)
				if event.object.from_id == 134371625 or event.object.from_id == 210101893:
					iq = random.randint(1000, 1500)
					self.send_message(event.object.peer_id, username + ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(podkr))
				elif event.object.from_id == 259758854:
					self.send_message(event.object.peer_id, username + ', ' + "тест на IQ пройден. Ваш результат: 1488228")
				elif iq <= 70:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqseventyn))
				elif iq <= 110:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqninty))
				elif iq >= 111:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqsuper))

			elif event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "монетка" or event.object.fwd_messages[0].text == "монетка":
				username = self.get_user_name(event.object.from_id)
				aa = random.randint(1, 2)
				if aa == 1:
					self.send_message(event.object.peer_id, username +  ', ' + "Выпал орел.\nПоздравляю, Вы отчислены!")
				else:
					self.send_message(event.object.peer_id, username +  ', ' + "Выпала решка.\nПоздравляю, Вы все равно отчислены!")

	def send_message(self, peer_id, message):
		self.vk_api.messages.send(peer_id=peer_id, random_id=0, message=message)

	def get_user_name(self, user_id):
		return self.vk_api.users.get(user_id=user_id)[0]['first_name']