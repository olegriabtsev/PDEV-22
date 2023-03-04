import telebot

TOKEN = "6038905745:AAGNXnU-u8xNjbT19QfWcA07nNKO0rE2I3g"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['voice'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет! У вас очень красивый голос!')


bot.polling(none_stop=True)
