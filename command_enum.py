def ttest(self, tterr):
	for tr in soup.find_all('tr', at_col = 't' + str(day + tterr)):
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