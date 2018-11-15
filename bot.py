import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
						  level = logging.INFO,
						  filename = 'bot.log'
						  )

def start_bot(bot, update):
	greeting_for_bot = """Darova, eto moi perviu bot.
On nechego poka ne umeet delat', toko commanda /game (net)"""
	update.message.reply_text(greeting_for_bot)

def chat(bot, update):
	user_text = update.message.text
	logging.info(user_text)
	update.message.reply_text(user_text)

def game_with_bot(bot, update):
	text_for_command_game = """Hochesh sigrat' so mnoi v igru? Okey.
Ya mogu ugadat' tvoe imya s pervoi popitki.. Smotri"""
	update.message.reply_text("""Tebya zovut: {},
izi je""".format(update.message.chat.first_name))

def main():
	upd = Updater(settings.TELEGRAM_API_KEY)

	upd.dispatcher.add_handler(CommandHandler("start", start_bot))
	upd.dispatcher.add_handler(CommandHandler("game", game_with_bot))
	upd.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	
	upd.start_polling()
	upd.idle()

if __name__ == "__main__":
	logging.info('Bot started')
	main()