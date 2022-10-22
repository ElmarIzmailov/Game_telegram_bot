from main1 import *
import telebot
from telebot import types
import time

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'game'])
def start(message):
    item = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("🧩 Pazl", callback_data=pazl)
    item2 = types.InlineKeyboardButton("🎓 Logica", callback_data=logica)
    item3 = types.InlineKeyboardButton("🚘 Drive cars", callback_data=car)
    item4 = types.InlineKeyboardButton("🪖 Action", callback_data=action)
    item5 = types.InlineKeyboardButton("🛀 Relaxation", callback_data=relaxs)
    item6 = types.InlineKeyboardButton("🏓 Sport", callback_data=sport)
    item7 = types.InlineKeyboardButton("⬅️ Back", callback_data=back)

    item.row(item1, item2)
    item.row(item3, item4)
    item.row(item5, item6)
    item.row(item7)
    bot.send_message(message.chat.id, f"😊 Hello {message.from_user.first_name}", reply_markup=item)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.send_message(call.message.chat.id, "🤔 Loading...")
    time.sleep(2.5)
    if call.data == pazl:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🕹 MainTower", url="https://gamezonebot.com/tower/")
            item2 = types.InlineKeyboardButton("🎮 MineRusher", url="https://gamezonebot.com/mine/")
            item.add(item1, item2)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == logica:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("2️⃣0️⃣4️⃣8️⃣", url="https://gamezonebot.com/2048")
            item2 = types.InlineKeyboardButton("🟨 Hextris", url="https://gamezonebot.com/hextris")
            item.add(item1, item2)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == car:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🏎 Adventure Drivers", url="https://games.cdn.famobi.com/html5games/a/adventure-drivers/v060/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=7adef9f1-9ddd-437a-b5ee-196da61ba5c7&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=545&original_ref=https%3A%2F%2Fgames.famobi")
            item2 = types.InlineKeyboardButton("🚓 Truck Trials", url="https://games.cdn.famobi.com/html5games/t/truck-trials/v510/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=e56b8aaa-86e9-4d9f-9ea1-3822a3021716&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=883&original_ref=https%3A%2F%2Fgames.famobi")
            item.add(item1, item2)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == action:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🦯 Stick", url="https://games.cdn.famobi.com/html5games/s/stick-freak/v010/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=40254c00-3fa9-42ac-9715-1583c4d57c7f&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=784&original_ref=https%3A%2F%2Fgames.cdn.famobi")
            item2 = types.InlineKeyboardButton("🕳 Color Tunnel", url="https://games.cdn.famobi.com/html5games/c/color-tunnel/v010/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=7bfb6b66-a75c-4021-af3f-ab7a6255186f&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=731&original_ref=#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DRBrSfohDIvrZrIpUzMfP")
            item.add(item1, item2)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == relaxs:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🐥 Flappy Bird", url="https://gamezonebot.com/floppybird/#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DcXiHlfChzXCntymfHkaZ")
            item.add(item1)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == sport:
        try:
            item = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("🏓 Table Tennis", url="https://games.cdn.famobi.com/html5games/t/table-tennis-world-tour/v370/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=8c8e5fc6-7e38-47ab-96eb-150276e79ef8&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=752&original_ref=https%3A%2F%2Ffamobi.com%2F#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DFnHULGsJVFWlyoQwzVRh")
            item2 = types.InlineKeyboardButton("🎯 Darts", url="https://games.cdn.famobi.com/html5games/0/3d-darts/v190/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=58bfd66f-ebc8-4b7e-be65-68ff573a11bf&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=779&original_ref=https%3A%2F%2Fgames.famobi.com%2F#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DDclnveZtBnaiTWrOTeXZ")
            item.add(item1, item2)
            bot.send_message(call.message.chat.id, f"🎮 Player {call.from_user.first_name}", reply_markup=item)
        except:
            bot.send_message(call.message.chat.id, f"😱 No info {call.from_user.first_name}")

    elif call.data == back:
        item = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("🧩 Pazl", callback_data=pazl)
        item2 = types.InlineKeyboardButton("🎓 Logica", callback_data=logica)
        item3 = types.InlineKeyboardButton("🚘 Drive cars", callback_data=car)
        item4 = types.InlineKeyboardButton("🪖 Action", callback_data=action)
        item5 = types.InlineKeyboardButton("🛀 Relaxation", callback_data=relaxs)
        item6 = types.InlineKeyboardButton("🏓 Sport", callback_data=sport)
        item7 = types.InlineKeyboardButton("⬅️ Back", callback_data=back)

        item.row(item1, item2)
        item.row(item3, item4)
        item.row(item5, item6)
        item.row(item7)
        bot.send_message(call.message.chat.id, f"Hello {call.from_user.first_name}", reply_markup=item)


bot.polling(none_stop=True)
