import telebot
bot = telebot.TeleBot('7856250351:AAHvjdmRwjBsAaFUfC0eNrTmUNEYQRmcGpM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Приветик! Выбери одну из оставшихся команд', parse_mode='Markdown')


@bot.message_handler(commands=['heart'])
def main_1(message):
    bot.send_message(message.chat.id, '*<3*', parse_mode='Markdown')


@bot.message_handler(commands=['question'])
def main_2(message):
    bot.send_message(message.chat.id, 'Чудо - это *ТЫ!*', parse_mode='Markdown')

bot.infinity_polling()