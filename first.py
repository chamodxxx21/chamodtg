import os
import telethon

bot = telebot, TeleBot ("API Key Here")

@bot .massage_handler(commands=["start"])
def send_welcome(massage):
    bot.reply_to(massage,"hello i am hackx bot"
   
   @bot.massage_handler(commands-["how"]) 
def send_massge(massage):
    bot.sent_massage(massage,"https://t.me/TheHackers_Grp")

   bot.polling()