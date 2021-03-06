import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bs4 import BeautifulSoup
import requests
import datetime
import json
import random
import time
import command_enum

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
			try:
				schedule_up = 'http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=0'
				schedule_down = 'http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=1'
				schedule = {'!в' : 0, '!н' : 1}
				text_schedule = ''
				a1 = []
				admins = [134371625]

				filename = "bd.txt"
				day = datetime.datetime.today().isoweekday()
				a3 = datetime.datetime.today().date()
				if day == 7:
					ofile = open(filename, 'r+')
					if a3.day % 2 == 0:
						a1.append(schedule_up)
					elif a3.day % 2 != 0:
						a1.append(schedule_down)
					json.dump(a1, ofile)
					ofile.close()

				elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text in schedule:
					if event.object.from_id == 134371625:
						ofile = open(filename, 'r+')
						a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=' + str(schedule[event.object.text]))
						json.dump(a1, ofile)
						ofile.close()
						alert_schedule = ""
						if schedule[event.object.text] == 0:
							alert_schedule = "верхнее"
						else:
							alert_schedule = "нижнее"

						self.send_message(event.object.peer_id, "Расписание изменено на " + alert_schedule)
					else:
						self.send_message(event.object.peer_id, "У вас нет доступа к данной команде")

				ofile = open(filename, 'r')
				json_data = json.load(ofile)
				html = requests.get(json_data[0]).text
				soup = BeautifulSoup(html, 'lxml')
				ofile.close()

				status = ""
				if json_data[0] == 'http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=0':
					status = "верхнее"
				else:
					status = "нижнее"

				if event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "!статус":
					self.send_message(event.object.peer_id, "Сейчас установлено " + str(status) + " расписание")

				rtime = datetime.datetime.today().time()
				times = datetime.time(12)

				if event.type == VkBotEventType.MESSAGE_NEW and "!кик" in event.object.text.lower():
					if event.from_chat:
						get_adm = self.get_user_admins(event.object.peer_id)
						for ttt in get_adm['items']:
							fff = ttt['chat_settings']
							sss = fff['owner_id']
							sas = fff['admin_ids']
							if event.object.from_id == sss or event.object.from_id in sas:
								try:
									userrr = event.object.text.lower().split("id")[1]
									userr = userrr.split('|')
									self.vk_api.messages.removeChatUser(chat_id=event.chat_id, user_id=userr[0])
								except IndexError:
									self.send_message(event.object.peer_id, "Вы указали неверный аргумент. \nВведите \"!кик @Имя_человека\" или \"!кик id + id_человека\"")
							else:
								self.send_message(event.object.peer_id, "У вас нет доступа к данной команде")
					else:
						self.send_message(event.object.peer_id, 'Данная команда доступна только в групповом чате')

				que = ['может сразу на завод пойдешь?', 'у меня нет слов, одни междометия', 'пожалуй, я промолчу', 'ну тут только в окно']
				iqseventyn = ['Не удивительно, что ты учишься в АПЭТ', 'Ну, бывает и хуже', 'Хотя бы не в минус', 'Странно, что ты вообще можешь связать речь..', 'IQ не зубы, еще вырастет']
				iqninty = ['Удивлен, что ты до сих пор учишься тут', 'Рад, что ты лучше некоторых', 'Даже у меня меньше', 'Для завода достаточно']
				iqsuper = ['Это что, Илон Маск?', 'Почему ты до сих пор живешь на земле?', 'Ты вообще с этой планеты?']

				bydn = "Расписание звонков в будни\n1 пара: 08:30-10:00\n2 пара: 10:10-11:40\n3 пара: 12:20-13:40\n4 пара: 13:50-15:10"
				subb = "Расписание звонков в субботу\n1 пара: 08:30-09:40\n2 пара: 09:50-11:00\n3 пара: 11:10-12:20\n4 пара: 12:30-13:40"

				daus = {'!расп понедельник': 1, '!расп вторник': 2, '!расп среда': 3, '!расп четверг': 4, '!расп пятница': 5, '!расп суббота': 6}

				if event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "!расп":
					if day <= 6 and rtime < times:
						trtr = command_enum.ttest(0)
						if day == 6:
							self.send_message(event.object.peer_id, subb + '\n\n' + text_schedule)
						else:
							self.send_message(event.object.peer_id, bydn + '\n\n' + text_schedule)

					elif day == 7:
						for tr in soup.find_all('tr', at_col = 't1'):
							try:
								zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
								kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
								zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
								kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2
								prep2 = tr.find('a')#Парсим преподавателей
								#prep = tr.find('a').findNext('a')#Парсим преподавателей

								if zan == None:
									text_schedule += zan2.text + '\nКабинет: ' + kab2.text + '\nПреподаватель: ' + prep2.text + '\n\n'
								else:
									text_schedule += zan.text + '\nКабинет: ' + kab.text + '\nПреподаватель: ' + prep2.text + '\n\n'
							except AttributeError:
								prep = ""
								prep2 = ""

						self.send_message(event.object.peer_id, bydn + '\n\n' + text_schedule)

					else:
						self.ttest(1)
						if day == 5 and rtime > times:
							self.send_message(event.object.peer_id, subb + '\n\n' + text_schedule)
						else:
							self.send_message(event.object.peer_id, bydn + '\n\n' + text_schedule)

				elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text in daus:
					for tr in soup.find_all('tr', at_col = 't' + str(daus[event.object.text])):
						try:
							zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
							kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
							zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
							kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2
							prep2 = tr.find('a')#Парсим преподавателей
							#prep = tr.find('a').findNext('a')#Парсим преподавателей

							if zan == None:
								text_schedule += zan2.text + '\nКабинет: ' + kab2.text + '\nПреподаватель: ' + prep2.text + '\n\n'
							else:
								text_schedule += zan.text + '\nКабинет: ' + kab.text + '\nПреподаватель: ' + prep2.text  + '\n\n'
						except AttributeError:
							prep = ""
							prep2 = ""

					self.send_message(event.object.peer_id, bydn + '\n\n' + text_schedule)


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


				elif event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "!созвать всех":
					if event.from_chat:
						if event.object.from_id == 134371625:
							get_user_ids = self.get_user_id(event.object.peer_id)
							users = ''
							for screen_name in get_user_ids['profiles']:
								try:
									username = screen_name['first_name']
									ids = screen_name['screen_name']
									users += '@' + str(ids) + '(' + username + ')' + ' '
								except KeyError:
									ids == screen_name['deactivated']
									continue
							self.send_message(event.object.peer_id, 'Вы были созваны для очень важного (нет) дела\n' + str(users))
						else:
							self.send_message(event.object.peer_id, 'У вас нет доступа к данной команде')
					else:
						self.send_message(event.object.peer_id, 'Данная команда доступна только в групповом чате')

				elif event.type == VkBotEventType.MESSAGE_NEW and (event.object.text).lower() == "монетка":
					username = self.get_user_name(event.object.from_id)
					aa = random.randint(1, 2)
					if aa == 1:
						self.send_message(event.object.peer_id, username +  ', ' + "Выпал орел.\nПоздравляю, Вы отчислены!")
					else:
						self.send_message(event.object.peer_id, username +  ', ' + "Выпала решка.\nПоздравляю, Вы все равно отчислены!")

			except requests.exceptions.ConnectionResetError:
				continue

	def send_message(self, peer_id, message):
		self.vk_api.messages.send(peer_id=peer_id, random_id=0,  message=message)

	def get_user_name(self, user_id):
		return self.vk_api.users.get(user_id=user_id)[0]['first_name']

	def get_user_id(self, peer_id):
		return self.vk_api.messages.getConversationMembers(peer_id=peer_id)

	def get_user_admins(self, peer_ids):
		return self.vk_api.messages.getConversationsById(peer_ids=peer_ids)