# Импортируем созданный нами класс Server
from a_pet import Server
# Получаем из config.py наш api-token
from config import vk_api_token


server1 = Server(vk_api_token, 167611254, "Бот A-PET")
# vk_api_token - API токен, который мы ранее создали
# 167611254 - id сообщества-бота
# "Бот A-PET" - имя сервера

server1.start()