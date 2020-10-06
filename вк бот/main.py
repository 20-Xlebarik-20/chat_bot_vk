import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import temo_po_name

# Индикатор работы сервера

print("Сервер запущен")

# Подключение бота к вк

token = "b4871d9d37b9171dc7ea6beab55c2bf44e5eae7a240af55520a1e8ee851a7d06d248534cccab015245468"
vk = vk_api.VkApi(token = token)
longpoll = VkLongPoll(vk)

# Функиця отправки сообщения в вк

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})

#  Прослушка сообщения, отпрвка сообщения

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            print("Новое сообщение! id: ", event.user_id)
            request = event.text.lower()

            # Узнавание города отправителя сообщения

            country = vk.method('users.get', {'user_ids': event.user_id, "fields": "city, country, bdate"})
            country = country[0]['city']['title']
            print("Город: ", country)

            # Узнаем имя отправителя

            name = vk.method('users.get', {'user_ids': event.user_id})
            name = name[0]['first_name']
            print("Имя отправителя: ", name)

            #Описание погоды

            description = temo_po_name(country)
            temp = description['temp']
            st = description['st']
            weather = ''

            if temp < 10:
                weather = 'Опа, а тут холодна... Температура: ' + str(temp)

            elif temp > 10:
                weather = 'Пипяо, тут аж жарко... Температура: ' + str(temp)

            # Ответы на сообщения

            if request == "привет" or request == "начать":
                write_msg(event.user_id, f'Хей уой, {name} , как ты? Наверное соскучился по мне?) Твой город: {country}, Верно?)  Да... Давно тут не был. Ну короч, давай поболтаем)')
                write_msg(event.user_id, 'Напиши "хелп", чтобы узнать, что я могу ')

            elif request == "как дела?":
                write_msg(event.user_id, "Нормально а у тебя как?)")

            elif request == "погода":
                write_msg(event.user_id, f"Хм... В твоем городе: {country} сейчас такая погода: \n {weather}")

            elif request == "что ты умеешь?" or request == "хелп":
                write_msg(event.user_id, "Хочешь узнать про мой функционал? Хм... Давай я тебе расскажу, что и как у меня тут все устроенно..." + "Мои команды: \n ○ Погода \n ○ Пока \n ○ Привет \n ○ Обратная связь(не работает временно) \n ○ Как дела?")

            elif request == "пока":
                write_msg(event.user_id, "Эх, жаль ты уходишь...Ну ладно давай пока...)")

            else:
                write_msg(event.user_id, "Ой, сори бро, не понел тебя... Скажи мне еще раз...")