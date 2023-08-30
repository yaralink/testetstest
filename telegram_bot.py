import telegram

bot = telegram.Bot(token="6494775844:AAH9Fbqpk7sxAjTP0BGyhdUH0Ql5BUiMILw")

def handle_message(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Hello!", reply_markup=telegram.ReplyKeyboardMarkup([
            telegram.KeyboardButton(text="Visit my website", url="https://www.dzibit.com")
        ]))

bot.message_loop(handle_message)
