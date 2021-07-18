import os
from os.path import join, dirname
from dotenv import load_dotenv
from clf_model.clf import text_clf
import constants
import telebot

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.chat.id, constants.START_COMMAND_MESSAGE)


@bot.callback_query_handler(func=lambda call: call.data in ['joy', 'anger', 'sadness', 'fear', 'love', 'surprise'])
def handle_feedback(call):
    chat_id, message = call.message.chat.id, call.message.text
    feedback = call.data
    # TODO create an api that will handle feedback
    bot.send_message(chat_id, f'Oke, so {message} is related to {feedback}. Ty')


@bot.message_handler(content_types=['text'])
def handle_text_prediction(message):
    prediction = text_clf.predict([message.text])
    bot.send_message(message.chat.id, f'I honestly think that you felt {prediction[0]}', reply_markup=constants.FEEDBACK_MARKUP)


if __name__ == '__main__':
    bot.polling()
