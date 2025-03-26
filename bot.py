from telebot import TeleBot

# Bot tokenini shu yerga qo‘ying
bot = TeleBot('7626797566:AAGDTS3ecJC5CBzg6V1eiedB5R3R4UKTas')

# /start komandasiga javob berish
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Salom! Men PUBG UC Donat botiman. Buyurtma berish uchun saytimizdan foydalaning: pubgdonat.tj")

# Har qanday xabarga javob berish
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
bot.infinity_polling()
