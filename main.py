from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import random 

import os

coins = ['1','2','5', '10']

command={'/start': 'Приветсвие',
         '/choice': 'Смена монетки'}

current_coin = 1

word = ['Бросок', 'бросок', 'подбрось', 'кинь']

updater = Updater(token='1521206514:AAEjmW5f3C0SIq5-KxEmftTLuf-Pzu4l30g', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!\nЯ идеальный помошник для тех, кто не может сделать выбор!\nПосмотреть все команды - /command")


def set_coin(update, context):
    global current_coin
    current_coin = (current_coin+1)%4
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Это твоя новая монетка!")
    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("img/"+coins[current_coin]+'_Russian_Reshka.png', 'rb'))


def on_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Подбрось счастливую монетку!")

def cast(update, context):
    a = random.randrange(2)
    if a==1:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("img/"+coins[current_coin]+'_Russian_Orel.png', 'rb'), caption = 'Орел')
    else: 
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("img/"+coins[current_coin]+'_Russian_Reshka.png', 'rb'),  caption = 'Решка')


def command_list(update, context):
    global command
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(command))


start_handler = CommandHandler('start', start)
set_coin_handler = CommandHandler('choice', set_coin)
get_command_list= CommandHandler('command',command_list )
cast_hendler = MessageHandler(Filters.text(word), cast)
message_handler = MessageHandler(Filters.text & (~Filters.command) & (~Filters.text(word)), on_message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(set_coin_handler)
dispatcher.add_handler(cast_hendler)
dispatcher.add_handler(get_command_list)
print('Bot started...')
updater.start_polling()
