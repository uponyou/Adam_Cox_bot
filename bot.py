import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

from datetime import datetime
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO, filename = 'bot.log')

def start_bot(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Darova, ti so mnoi seichas budesh obshatsa. Ti menya ponyal?')

def chatting(bot, update):
	request = apiai.ApiAI('SOME_API_KEY').text_request()
	request.lang = 'ru'
	request.session_id = 'BatlabAIBot'
	request.query = update.message.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
	else:
		bot.send_message(chat_id=update.message.chat_id, text='ti che nesesh? Ya tebe je po ruski govoru..') 

def main():
	upd = Updater(settings.TELEGRAM_API_KEY)
	dispatcher = upd.dispatcher

	dispatcher.add_handler(CommandHandler("start", start_bot))	
	dispatcher.add_handler(MessageHandler(Filters.text, chatting))
	
	upd.start_polling(clean=True)
	upd.idle()

if __name__ == "__main__":
	logging.info('Bot started')
	main()
	
