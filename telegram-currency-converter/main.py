import telebot
from extensions import Price, APIException


bot = telebot.TeleBot(open("token", "r").read())


@bot.message_handler(commands=['start', 'help'])
def startCommandsHandler(message):
    try:
        output = open("startMessage.txt", "r").read()
    except Exception as e:
        output = e
    bot.send_message(message.chat.id, output)


@bot.message_handler(commands=['values'])
def valuesCommandHandler(message):
    try:
        rates = Price.get_rates()
        keys = rates.keys()
        output = ""
        for key in keys:
            output += str(round(rates[key], 2))+" "+key + "\n"
    except Exception as e:
        output = e
    bot.send_message(message.chat.id, output)


@ bot.message_handler(content_types=['text'])
def messageHandler(message):
    try:
        messageText = message.text.split()
        if len(messageText) > 3:
            raise APIException('Too many arguments')
        if len(messageText) < 3:
            raise APIException('Not enough arguments')
        output = Price.get_price(
            messageText[0], messageText[1], messageText[2])
    except Exception as e:
        output = e
    bot.send_message(message.chat.id, output)


bot.polling()
