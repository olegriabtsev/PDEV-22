import telebot

TOKEN = '6038905745:AAGNXnU-u8xNjbT19QfWcA07nNKO0rE2I3g'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.text)
    bot.reply_to(message, f'Welcome, {message.chat.username}')


@bot.message_handler(content_types=['document', 'audio'])
def handler_docs_audio(message):
    pass


@bot.message_handler(content_types=['photo'])
def send_picture(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
