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
			day = datetime.datetime.today().weekday()
			a3 = datetime.datetime.today().date()
			if day == 6:
				a1 = []
				ofile = open(filename, 'r+')
				if day == 6 and a3.day % 2 == 0:
					a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=1')
				elif day == 6 and a3.day % 2 != 0:
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

			'''iq = [45, 23, 76, 57, 49, 15, 0, 65, 46, 17, 3]'''

			que = ['может сразу на завод пойдешь?', 'у меня нет слов, одни междометия', 'пожалуй, я промолчу', 'ну тут только в окно']
			iqseventyn = ['Не удивительно, что ты учишься в АПЭТ', 'Ну, бывает и хуже', 'Хотя бы не в минус', 'Странно, что ты вообще можешь связать речь..', 'IQ не зубы, еще вырастет']
			iqninty = ['Удивлен, что ты до сих пор учишься тут', 'Рад, что ты лучше некоторых', 'Даже у меня меньше', 'Для завода достаточно']
			iqsuper = ['Это что, Илон Маск?', 'Почему ты до сих пор живешь на Земле?', 'Ты вообще с этой планеты?']

			bydn = "Расписание звонков в будни\n1 пара: 08:30-10:00\n2 пара: 10:10-11:40\n3 пара: 12:20-13:40\n4 пара: 13:50-15:10"
			subb = "Расписание звонков в субботу\n1 пара: 08:30-09:40\n2 пара: 09:50-11:00\n3 пара: 11:10-12:20\n4 пара: 12:30-13:40"

			#while event.object.text != "отмена":
			'''game2 = random.randint(1, 3)
			if game2 == 1:
				pl1 = " &#128074;"
			elif game2 == 2:
				pl1 = " :v:"
			else:
				pl1 = " &#9995;"

			if event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!кнб":
				self.send_message(event.object.peer_id, "Выберите один из трех предметов. \n 1 - 👊 2 - ✌ 3 - ✋")
				try:
					if event.object.text == "1":
						self.send_message(event.object.peer_id, "Вы выбрали &#128074;\n Бот выбрал" + str(pl1))
						if game2 == 1:
							self.send_message(event.object.peer_id, "Ничья")
						elif game2 == 2:
							self.send_message(event.object.peer_id, "Вы Победили")
						else:
							self.send_message(event.object.peer_id, "Вы проиграли")

					elif event.object.text == "2":
						self.send_message(event.object.peer_id, "Вы выбрали :v:\n Бот выбрал" + str(pl1))

						if game2 == 1:
							self.send_message(event.object.peer_id, "Вы проиграли")
						elif game2 == 2:
							self.send_message(event.object.peer_id, "Ничья")
						else:
							self.send_message(event.object.peer_id, "Вы Победили")

					elif event.object.text == "3":
						self.send_message(event.object.peer_id, "Вы выбрали &#9995;\n Бот выбрал" + str(pl1))
						if game2 == 1:
							self.send_message(event.object.peer_id, "Вы Победили")
						elif game2 == 2:
							self.send_message(event.object.peer_id, "Вы прроиграли")
						else:
							self.send_message(event.object.peer_id, "Ничья")

					elif event.object.text == "отмена":
						self.send_message(event.object.peer_id, "Выход из игры")

					else:
						self.send_message(event.object.peer_id, "Выберите предметы от 1 до 3")
						pass
						continue
				except:
					self.send_message(event.object.peer_id, "Выберите предметы от 1 до 3")'''


			if event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп":

				if day == 0:
					if rtime <= times:
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
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't2'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 1:
					if rtime <= times:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't2'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')
					else:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't3'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 2:
					if rtime <= times:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't3'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')
					else:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't4'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 3:
					if rtime <= times:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't4'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')
					else:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't5'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 4:
					if rtime <= times:
						self.send_message(event.object.peer_id, bydn)
						for tr in soup.find_all('tr', at_col = 't5'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')
					else:
						self.send_message(event.object.peer_id, subb)
						for tr in soup.find_all('tr', at_col = 't6'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 5:
					if rtime <= times:
						self.send_message(event.object.peer_id, subb)
						for tr in soup.find_all('tr', at_col = 't6'):
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

							if zan == None:
								self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
							else:
								self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

				elif day == 6:
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


								'''ТУПА ИЗИ, ТУПА СПЛЕШ, ТУПА ЕБЛАН НА ВАЛЕРЕ УЧИСЬ ДЕЛАТЬ МЕНЬШЕ КОДА
									НАДО КАК-ТО ЭТО ЕБАТЬ УЖАТЬ ПИЗДЕЦ КАК, ЧТОБ ОНО НЕ ЗАНИМАЛО МИЛЛИОН СТРОК СУКА ТУПАЯ'''
								

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп понедельник":
				for tr in soup.find_all('tr', at_col = 't1'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп вторник":
				for tr in soup.find_all('tr', at_col = 't2'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп среда":
				for tr in soup.find_all('tr', at_col = 't3'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп четверг":
				for tr in soup.find_all('tr', at_col = 't4'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп пятница":
				for tr in soup.find_all('tr', at_col = 't5'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп суббота":
				for tr in soup.find_all('tr', at_col = 't6'):
					zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
					kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
					zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
					kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

					if zan == None:
						self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
					else:
						self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!расп воскресенье":
				username = self.get_user_name(event.object.from_id)
				self.send_message(event.object.peer_id, username +  ', ' + random.choice(que))

			elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "!iq" or event.object.text == "!айку":
				username = self.get_user_name(event.object.from_id)

				iq = random.randint(1, 150)
				iqq = random.randint(1000, 1500)
				if iq <= 70:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqseventyn))
				elif iq <= 110:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqninty))
				elif iq >= 111:
					self.send_message(event.object.peer_id, username +  ', ' + "тест на IQ пройден. Ваш результат: " + str(iq) + "\n" + random.choice(iqsuper))
				elif username == "Александра":
					self.send_message(event.object.peer_id, username + ', ' + "тест на IQ пройден. Ваш результат: " + str(iqq) + "\n" + 'Ну это просто бог какой-то')

	def send_message(self, peer_id, message):
		self.vk_api.messages.send(peer_id=peer_id, random_id=0, message=message)

	def get_user_name(self, user_id):
		return self.vk_api.users.get(user_id=user_id)[0]['first_name']