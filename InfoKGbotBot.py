from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from pyrogram.types import ChatPermissions
import time
import asyncio 
import os

app = Client(
    "my_bot",
    bot_token = "1940303458:AAFTeAtPHmz2VB4hg-Ccgi49l-B0lSJStCM"
    api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e",                                                                                                                   
    api_id = 6
)

#ПРивет
@app.on_message(filters.regex(r"[Пп][Рр][Ии][Вв][Ее][Тт] [Кк][Оо][Тт]"))
@app.on_message(filters.regex(r"[Дд][Аа][Рр][Оо][Вв][Аа], [Кк][Оо][Тт]"))
@app.on_message(filters.regex(r"[Пп][Рр][Ии][Вв][Ее][Тт], [Кк][Оо][Тт]"))
@app.on_message(filters.regex(r"[Дд][Аа][Рр][Оо][Вв][Аа] [Кк][Оо][Тт]"))
async def func(app,msg):
     await msg.reply(f"Привет, {msg.from_user.mention}")
        
@app.on_message(filters.regex(r"/start") & filters.private)
async def func1(app,msg):
    await msg.reply(f"__**Привет, я - бот инструктор по установке Kgbot^a.\nМои команды:__**\n**__/instruction__**")
    
@app.on_message(filters.regex(r"/instruction") & filters.private)
async def func1(app,msg):
  await app.send_message(msg.chat.id,"__**Хорошо, Kgbot'а можно поставить через приложение [Termux](https://play.google.com/store/apps/details?id=com.termux) и сайт replit.com, какой способ выбираете?**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Поставить через приложение Termux"],
      ["Поставить через сайт Repl.it"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))

@app.on_message(filters.regex(r"Поставить через сайт Repl.it") & filters.private)
async def func6(app,msg):
  await app.send_message(msg.chat.id,"__**Для этого вам необходимо зарегестрироваться на сайте <u>replit.com</u>**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Зарегестрировался"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))

@app.on_message(filters.regex(r"Зарегестрировался") & filters.private)
async def func7(app,msg):
  await app.send_message(msg.chat.id,"__**После регестрации перейдите по ссылке <u>https://replit.com/github/cemiix/kgbotpublic</u> и запустите(Зеленая кнопочка.)**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Дальше"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))

@app.on_message(filters.regex(r"Дальше") & filters.private)
async def func8(app,msg):
  await app.send_message(msg.chat.id,"__**После успешной авторизации бота, в консоли должна появиться ссылка, берем её и идем на сайт <u>UptimeRobot.com</u>**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Дaльше"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))

@app.on_message(filters.regex(r"Дaльше") & filters.private)
async def func9(app,msg):
  await app.send_message(msg.chat.id,"__**Регистрируемся или Входим в свой аккаунт, нажимаем <code>Add New Monitor</code>, выбираем тип монитора <code>HTTP(S)</code>, имя монитора какое хотите, а в поле url, вставляем ссылку, которую мы получили после авторизации бота**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Готово"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))
@app.on_message(filters.regex(r"Готово") & filters.private)
async def func10(app,msg):
 await app.send_message(msg.chat.id,"__**Готово(Не забудьте написать свой номер телефона и код.)\nАвторы юзербота: @cemiix, @pomyanem_ne_tegai\nАвтор бота: @qotenok\nЕсли вдруг возникнет ошибка пишите: https://t.me/kgbot_modules\nКанал с модулями: https://t.me/kgbotmodules**__",
 reply_markup = ReplyKeyboardMarkup(
     [
      ["", "Поставить через приложение Termux"],
      ["Поставить через сайт Repl.it"],
      
    ],
 resize_keyboard = True,
one_time_keyboard = True
  ))


@app.on_message(filters.regex(r"Поставить через приложение Termux") & filters.private)
async def func2(app,msg):
  await app.send_message(msg.chat.id,"__**Для этого вам необходимо установить на свой телефон приложение Termux.**__",
        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Установил"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))

@app.on_message(filters.regex(r"Установил") & filters.private)
async def func3(app,msg):
  await app.send_message(msg.chat.id,"__**Введите следующие команды:**__\n <code>apt update\napt upgrade\npkg install git python\npip install pyrogram\npip install meval\npip install tgcrypto\npip install wheel\npip install Pillow</code>",

        reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Написал"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))


@app.on_message(filters.regex(r"Написал") & filters.private)
async def func4(app,msg):
  await app.send_message(msg.chat.id,"__**После всего этого пишем:**__\n<code>git clone https://github.com/Laimusp/KGBotPublic && cd KGBotPublic</code>\n__**И наконец прописываем:**__ <code>python main.py</code>\n**__Авторы юзербота: @cemiix, @pomyanem_ne_tegai\nАвтор бота: @qotenok\nЕсли вдруг возникнет ошибка пишите: https://t.me/kgbot_modules\nКанал с модулями: https://t.me/kgbotmodules__**",
   reply_markup = ReplyKeyboardMarkup(
    [
      ["", "Поставить через приложение Termux"],
      ["Поставить через сайт Repl.it"],
      
    ],
resize_keyboard = True,
one_time_keyboard = True
  ))
@app.on_message(filters.user(1873467850) & filters.reply & filters.regex(r"[Оо]к"))
@app.on_message(filters.user(1873467850) & filters.reply & filters.regex(r"[Нн][Ее] [Яя]"))
@app.on_message(filters.user(1873467850) & filters.reply & filters.regex(r"[Мм][Аа][Фф]"))
@app.on_message(filters.user(1873467850) & filters.reply & filters.regex(r"[Дд][Оо][Кк]"))
@app.on_message(filters.user(1873467850) & filters.reply & filters.regex(r"[Гг]о"))
async def func5(app,msg):
  await msg.reply("Бот на тех-работах")
  await app.restrict_chat_member(msg.chat.id,msg.reply_to_message.from_user.id,ChatPermissions(can_send_messages=False),until_date=round(time.time()+100000))
  

@app.on_message(filters.user(1186358927) & filters.reply  & filters.regex(r"[Кк][Уу][Сс][Ьь] [Аа][Тт][Ии][Кк][Аа]"))
@app.on_message(filters.reply  & filters.regex(r"[Кк][Уу][Сс][Ьь] [Аа][Тт][Ии][Кк][Аа]"))
async def func5(app,msg):
  await msg.reply("КУСЬ ЛЕГЕНДАРНОГО АТИКА")
  await app.restrict_chat_member(msg.chat.id,msg.reply_to_message.from_user.id,ChatPermissions(can_send_messages=False),until_date=round(time.time()+100000))
  await msg.reply("УКУСИИЛ!!!!!")


app.run()
