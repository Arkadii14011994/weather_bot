import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

infor = []
@bot.message_handler(commands=['start'])


def welcome(message):
    menu = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton("ФИО",callback_data="full_name")
    b2 = types.InlineKeyboardButton("Возраст",callback_data="age")
    b3 = types.InlineKeyboardButton("телефон\имаэл",callback_data="mail")
    menu.add(b1,b2,b3)
    link = "https://ru.pngtree.com/freebackground/picture-of-a-blue-bird-on-a-black-background_3124189.html"
    bot.set_webhook(message.chat.id,link)
    bot.send_message(message.chat.id,f"<b>Доборо пожаловать {message.from_user.username} </b>",parse_mode="html",reply_markup=menu)


@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    if call.data == "full_name":
        bot.send_message(call.message.chat.id,"<b>Введите ФИО(полностью)   :</b>",parse_mode='html')
    elif call.data == "age":
        bot.send_message(call.message.chat.id,"<b>ваш возраст?</b>",parse_mode='html')
    elif call.data == "mail":
        bot.send_message(call.message.chat.id,"<b>Введите телефон либо mail   :</b>",parse_mode='html')

@bot.message_handler(func=lambda message:True)

def input_info(message):
    if message.text is not None:
        infor.append(message.text)
        bot.send_message(message.chat.id,"данные сохранены")
    save()
def save():
    if len(infor)>=3:
        with open("customer.txt","a") as f:
            f.write(f"фио {infor[0]}\n")
            f.write(f"возраст {infor[1]}\n")
            f.write(f"почта\телефон {infor[2]}\n")
    else:
        print("не полных данных")




bot.polling(non_stop=True)
