from telegram.ext import Updater , CommandHandler , MessageHandler , Filters, CallbackQueryHandler
from functions import *
from const import *
updater = Updater(token = TOKEN , workers = 5)
dispatcher = updater.dispatcher
dispatcher.add_handler(CallbackQueryHandler(pattern='gift', callback=gift))
dispatcher.add_handler(CallbackQueryHandler(pattern='calendars', callback=calendars))
dispatcher.add_handler(CommandHandler(command = "start" , callback = start))
dispatcher.add_handler(CommandHandler(command = "buttons" , callback = buttons))
dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=text_answ, run_async=True))
updater.start_polling(drop_pending_updates=True)
updater.idle()