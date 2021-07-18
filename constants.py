from telebot import types
START_COMMAND_MESSAGE = "Hi, this bot's main function is to classify emotions from some given text. Dataset used for this bot is pretty " \
                        "freaking bad... And well the person, who created the model is kinda hopeless in terms of ml as well. At least help me out by giving " \
                        "actual feedback to my prediction to help me learn."

EXPLANATION = 'My main function is to predict what emotions have you put into the text. I am able to guess 4 main types of ' \
              'emotions: anger, fear, joy, love, sadness, surprise. At the end of my guess I would like you to give me some feedback, whether ' \
              'I was correct or not. I should learn after all :)'




# Feedback markup
FEEDBACK_MARKUP = types.InlineKeyboardMarkup()
joy = types.InlineKeyboardButton('joy', callback_data='joy')
fear = types.InlineKeyboardButton('fear', callback_data='fear')
sadness = types.InlineKeyboardButton('sadness', callback_data='sadness')
anger = types.InlineKeyboardButton('anger', callback_data='anger')
love = types.InlineKeyboardButton('love', callback_data='love')
surprise = types.InlineKeyboardButton('surprise', callback_data='surprise')
FEEDBACK_MARKUP.row(joy, fear, love)
FEEDBACK_MARKUP.row(sadness, anger, surprise)
