import requests
from bs4 import BeautifulSoup
import datetime


class Weather:
    @staticmethod
    def get_weather_today():
        a3 = datetime.datetime.today().date()
        day = datetime.datetime.today().weekday()
        if day == 6 and a3.day % 2 == 0:
            test = 1
        elif day == 6 and a3.day % 2 != 0:
            test = 0

        html = requests.get("http://a-pet.ru/schedule/?group=%CF%CA%D1-7&even=1").text
        soup = BeautifulSoup(html, 'lxml')

        for tr in soup.find_all('tr', at_col = 't3'):
            zan = tr.find('td', class_ = 'sch_ed')#Парсим занятие
            kab = tr.find('td', class_ = 'sch_ed sch_room')#Парсим кабинеты
            zan2 = tr.find('td', class_ = 'sch_all')#Парсим занятие, если их 2
            kab2 = tr.find('td', class_ = 'sch_all sch_room')#Парсим кабинеты, если их 2

            if zan == None:
                result = (zan2.text + '\n' 'Кабинет: ' + kab2.text + '\n')
            else:
                result1 = (zan.text + '\n' 'Кабинет: ' + kab.text + '\n')



