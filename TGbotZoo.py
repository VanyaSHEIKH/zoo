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
    elif message.text == "👉 Давай начнем наш тест 👈":
        send_question(message.chat.id)
    else:
        bot.send_message(message.chat.id,text="Такой командой я пока не умею пользоваться")

current_question_index = 0
user_answers = []

# Функция для обработки ответов пользователя
@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    global current_question_index, user_answers

    if message.text == "👉 Давай начнем наш тест 👈":
        send_question(message.chat.id)
    elif current_question_index < len(questions):
        user_answers.append(message.text)
        current_question_index += 1
        send_question(message.chat.id)
    else:
        bot.send_message(message.chat.id, f"Спасибо за участие в тесте! Ваши ответы: {', '.join(user_answers)}")



# Функция для отправки вопроса и кнопок с вариантами ответов
def send_question(chat_id):
    question_data = questions[current_question_index]
    question = question_data["question"]
    answers = question_data["answers"]

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for answer in answers:
        markup.add(types.KeyboardButton(answer))

    msg=bot.send_message(chat_id, text=question, reply_markup=markup)
    bot.register_next_step_handler(msg,send_question)

bot.infinity_polling()



