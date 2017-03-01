# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
import configparser
import logging
from telegram import ChatAction

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)

config = configparser.ConfigParser()
config.read('bot.ini')


updater = Updater(token=config['BOT']['TOKEN'])
dispatcher = updater.dispatcher
help_text="""
[ x ] /invitelink  --> Prints the invite link to this group
[ x ] /googleform  --> Link to the Google Form
[ x ] /googlegroup  --> Link to the Google Group
[ x ] /facebook    --> Facebook Group of Open3Source
"""

def invitelink(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['invite_link'])

def fbgroup(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['fbgroup'])

def googleform(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id,
                       action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=config['BOT']['googleform'])

def googlegroup(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=comfig['BOT']['googlegroup'])

def help(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.sendMessage(chat_id=update.message.chat_id, text=help_text,parse_mode='Markdown')

invite_handler = CommandHandler('invitelink',invitelink)
fbgroup_handler = CommandHandler('facebook',fbgroup)
googleform_handler = CommandHandler('googleform',googleform)
googlegroup_handler = CommandHandler('googlegroup',googlegroup)
help_handler = CommandHandler('help',help)

dispatcher.add_handler(invite_handler)
dispatcher.add_handler(fbgroup_handler)
dispatcher.add_handler(googleform_handler)
dispatcher.add_handler(googlegroup_handler)
dispatcher.add_handler(help_handler)


updater.start_polling()
updater.idle()
