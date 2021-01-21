from car_info import get_car_info
from config import config
import telebot

bot = telebot.TeleBot(config.telebotToken)

prepped_strings = {
    'url': 'Посилання: %s',
    'sold': 'Вже продано: %s',
    'added': 'Опубліковано: %s',
    'last_updated': 'Оновлено: %s',
    'phone': 'Телефон продавця: %s',
    'location': 'Місто: %s',
    'price': 'Ціна: %s',
    'year': 'Рік випуску: %s',
    'odometer': 'Пробіг: %s',
    'fuel': 'Тип палива: %s',
    'gear': 'Коробка передач: %s',
    'vin': 'VIN-код: %s',
    'plate': 'Номер: %s',
}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Відправ мені посилання сторінки авта на autoRia або його ID,"
                          "і я покажу інформацію про нього та VIN-код")


@bot.message_handler(func=lambda message: True)
def return_car_info(message):
    if message.text:
        carInfo = get_car_info(message.text)
        if carInfo:
            reply_lst = list()
            reply_lst.append(prepped_strings['sold'] % ('так' if carInfo.sold else 'ні'))
            for key in prepped_strings:
                value = getattr(carInfo, key)
                if value:
                    reply_lst.append(prepped_strings[key] % value)

            this_reply_string = '\n'.join(reply_lst)
            bot.reply_to(message, this_reply_string)
        else:
            bot.reply_to(message, 'Відповіді не знайдено')
    else:
        bot.reply_to(message, 'Твоє повідомлення пусте')


bot.polling()
