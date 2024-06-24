import telebot
from config import TOKEN
from telebot import types
from questions import questions
bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("👋 Поздороваться")
    button2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(button1, button2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот, который поможет тебе подобрать твое 'тотемное животное'.".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=["text"])
def func(message):
    if (message.text=="👋 Поздороваться"):
        bot.send_message(message.chat.id,text="Привеееет...")
    elif (message.text=="❓ Задать вопрос"):
        bot.send_message(message.chat.id,text="Чем я могу помочь?")
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1=types.KeyboardButton("💬 Кто я и для чего я нужен?")
        button2=types.KeyboardButton("🐬 Что за 'тотемное животное'?")
        button3=types.KeyboardButton("🤪 Нажми меня!")
        back=types.KeyboardButton("🏠︎ Вернуться в главное меню")
        markup.add(button1,button2,button3,back)
        bot.send_message(message.chat.id,text="Задай мне вопрос",reply_markup=markup)
    elif (message.text=="💬 Кто я и для чего я нужен?"):
        bot.send_message(message.chat.id,text="У меня нет имени, но, возможно, нам с тобой получится придумать мне имя после сомествной работы🤔.\
 Я был создан, чтобы помочь тебе определиться со своим 'тотемным животным'.")
    elif (message.text=="🐬 Что за 'тотемное животное'?"):
        bot.send_message(message.chat.id,text="Всё вокруг нас является энергией, которая собирается в клубки. Она окутывает окружающие предметы, может давать им силу или, наоборот, отнимать её.\
 Существует также понятие «эгрегор» — это общее биополе, которое создается мыслями определенной группы.\
 На протяжении тысячелетий людьми создавались эгрегоры тотемных животных. Это тоже сгустки энергии, которые обладают характеристиками разных животных, птиц и насекомых. Они не умеют в прямом смысле прыгать как заяц или летать как голубь.\
 Тотемное животное — это покровитель, который наделяет человека теми качествами, которыми обладает сам.\
 Он даёт человеку энергию для выполнения конкретного действия в физическом мире.")
    elif (message.text=="🤪 Нажми меня!"):
        bot.send_message(message.chat.id,text="🗿")
    elif (message.text=="🏠︎ Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        starter = types.KeyboardButton("👉 Давай начнем наш тест 👈")
        markup.add(button1, button2,starter)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню, и теперь мы готовы приступить к тесту 'Какое у вас тотемное животное'!" ,reply_markup=markup)
    else:
        bot.send_message(message.chat.id,text="Такой командой я пока не умею пользоваться")
# @bot.message_handler(func=lambda message: message.text == "👉 Давай начнем наш тест 👈")
# def test(message:telebot.types.Message):
#     for question in questions.keys():
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("")
#         button2 = types.KeyboardButton(" ")
#         button3 = types.KeyboardButton(" ")
#         back = types.KeyboardButton(" ")
#         markup.add(button1, button2, button3, back)
#         bot.send_message(message.chat.id, text=question, reply_markup=markup)
#         for question in questions.keys():
#             bot.register_next_step_handler(message,test)

current_question_index = 0

@bot.message_handler(func=lambda message: message.text == "👉 Давай начнем наш тест 👈")
def start_test(message):
    send_question(message.chat.id)
def send_question(chat_id):
    global current_question_index
    if current_question_index < len(questions):
        question = list(questions.keys())[current_question_index]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Ответ 1")
        button2 = types.KeyboardButton("Ответ 2")
        button3 = types.KeyboardButton("Ответ 3")
        button4 = types.KeyboardButton("Ответ 4")
        markup.add(button1, button2, button3, button4)
        bot.send_message(chat_id, text=questions[question], reply_markup=markup)
        current_question_index += 1
    else:
        bot.send_message(chat_id, text="Тест завершен. Спасибо за участие!")

@bot.message_handler(func=lambda message: message.text in ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4"])
def handle_answer(message):
    send_question(message.chat.id)


bot.infinity_polling()





