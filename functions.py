from time import sleep
from const import *
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from sql_req import *
# from apscheduler.schedulers import
# sched = Scheduler()
# sched.start()

def users(update, context):
    user_id = update.message.chat_id
    text = update.message.text
    first_name = update.message.from_user.first_name
    return user_id, text, first_name

def start(update , context) :
    user_id, text, first_name = users(update,context)
    context.bot.send_message(text=OK_msg, chat_id = user_id)


def send_cont(update,context):
    user_id = update.callback_query.from_user.id
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    l = cursor.execute(lang_in_table.format(user_id)).fetchall()
    l = l[0][0]
    b = [KeyboardButton(text=GLOBAL_DCT[l][1], request_contact=True)]
    context.bot.send_message(text=GLOBAL_DCT.get(l)[0], reply_markup=ReplyKeyboardMarkup([b]), chat_id=user_id)

def text_answ(update , context) :
    user_id, text, first_name = users(update,context)
    text = str(text)
    context.bot.send_chat_action(chat_id=user_id, action=telegram.ChatAction.TYPING)
    sleep((0.7))
    if text in DCT.keys():
        context.bot.send_message(text=DCT.get(text), chat_id=user_id)
    else:
        context.bot.send_message(text='Я тебя не поняла', chat_id=user_id)


def buttons (update, context):
    user_id, text, first_name = users(update, context)
    b = [KeyboardButton(text='Выбери мне подарок', callback_data='gift')]
    c = [KeyboardButton(text='Наш календарь', callback_data='calendars')]
    context.bot.send_message(chat_id=user_id, text='Есть проблема?', reply_markup=ReplyKeyboardMarkup([b,c], resize_keyboard=True, one_time_keyboard=True))

def gift (update, context):
    user_id, text, first_name = users(update, context)
    b = [
        InlineKeyboardButton(text='Духи Coco mademoiselle by Chanel', callback_data='perfume'),
        InlineKeyboardButton(text='Браслет Гвоздь от Cartier', callback_data='bracelet'),
        InlineKeyboardButton(text='Лодочки от Louboutin', callback_data='shoes'),
        InlineKeyboardButton(text='Букет огромных роз', callback_data='roses')]
    context.bot.send_message(chat_id=user_id, text='Выбери мне подарок:', reply_markup=InlineKeyboardMarkup([b]))


def calendars (update, context):
    user_id, text, first_name = users(update, context)
    c = [
        InlineKeyboardButton(text='Посмотреть ваши даты', callback_data='mydates'),
        InlineKeyboardButton(text='Добавить новое событие', callback_data='addevent')]
    context.bot.send_message(chat_id=user_id, text='Вспомнить наши важные даты:', reply_markup=InlineKeyboardMarkup([c]))


def perfume (update, context):
    user_id, text, first_name = users(update, context)
    context.bot.send_message()