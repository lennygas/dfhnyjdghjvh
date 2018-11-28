import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bs4 import BeautifulSoup
import requests
import datetime
import json

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
    			if a3.day % 2 == 0:
    				a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=1')
    			else:
    				a1.append('http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=0')
    			json.dump(a1, ofile)
    			ofile.close()
    		ofile = open(filename, 'r')
    		json_data = json.load(ofile)
    		html = requests.get(json_data[0]).text
    		soup = BeautifulSoup(html, 'lxml')
    		#ofile.close()

    		if event.type == VkBotEventType.MESSAGE_NEW and event.object.text == "расписание":
    			rtime = datetime.datetime.today().time()
    			times = datetime.time(15)

    			if day == 0:
    				if rtime <= times:
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
    					for tr in soup.find_all('tr', at_col = 't3'):
    						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
    						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
    						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
    						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

    						if zan == None:
    							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n' + str(rtime))
    						else:
    							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n' + str(rtime))
    				else:
    					for tr in soup.find_all('tr', at_col = 't4'):
    						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
    						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
    						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
    						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

    						if zan == None:
    							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n' + str(rtime))
    						else:
    							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n' + str(rtime))

    			elif day == 3:
    				if rtime <= times:
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
    				if rtime <= datetime.time(16):
    					self.send_message(event.object.peer_id, f"Я еще не обновил расписание на завтра, додлитесь 16:00")
    				else:
    					for tr in soup.find_all('tr', at_col = 't1'):
    						zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
    						kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
    						zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
    						kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

    						if zan == None:
    							self.send_message(event.object.peer_id, zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
    						else:
    							self.send_message(event.object.peer_id, zan.text + '\n' 'Кабинет: ' + kab.text + '\n')

    def send_message(self, peer_id, message):
    	self.vk_api.messages.send(peer_id=peer_id, random_id=0, message=message)

    def get_user_name(self, user_id):
    	return self.vk_api.users.get(user_id=user_id)[0]['first_name']