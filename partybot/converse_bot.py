#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
#import game_host

#pip install -r requirements.txt
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

answers = {"counter": 0}

questions = ["Do you want to split the bill equally",
             "How much is the bill?",
             "How many people are in table?"]


def greet(msg):
    greeting_msg = "Hello I am a gamebot, I will ask you some questions about the game. If you don't want to answer just say no."
    human_greetings = ["hello", "hi", "hey"]
    if msg.lower() in human_greetings:
        return greeting_msg
    else:
        return None


def negative(msg):
    if msg.lower() == "no":
        answers["counter"] = 0
        return "Thank you!"
    else:
        return None

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def bill_equal_split(answers):
    total_bill = int(answers[0])
    no_of_people = int(answers[1])
    per_head = total_bill/no_of_people
    reply = f"per head bill {per_head}"
    return reply


def echo(bot, update):
    """Echo the user message."""
    msg = update.message.text
    #output = game_host.identify_msg(msg)
    greeting = greet(msg)
    thank_you = negative(msg)
    if greeting:
        answer = greeting
    elif thank_you:
        answer = thank_you
    elif answers["counter"] == len(questions):
        question_number = answers["counter"] - 1
        answers[question_number] = msg
        answer = bill_equal_split(answers)
        # reply = "Thank you! Enjoy your game."
        # answer = reply
        answers["counter"] = 0
        print(answers)
    else:
        counter = answers["counter"]

        if counter > 0:
            question_number = counter - 1
            answers[question_number] = msg
        else:
            pass
        question = questions[counter]
        answers["counter"] += 1
        answer = question
    update.message.reply_text(answer)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    TOKEN = "730572026:AAH49UZ2KyyQhMWDmhP205uIARJKtw6I3NU"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
