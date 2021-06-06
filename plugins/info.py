# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  info.py importado.{/cyan}'))

markup = types.InlineKeyboardMarkup()
b1 = types.InlineKeyboardButton(
    "Channel", url="https://telegram.me/league_of_legends_channel")
b2 = types.InlineKeyboardButton("Developer", url="https://telegram.me/edurolp")
b3 = types.InlineKeyboardButton(
    "GitHub", url="https://github.com/i32ropie/lol")
markup.add(b1, b2, b3)
b4 = types.InlineKeyboardButton("PayPal", url="https://paypal.me/edurolp")
markup.add(b4)


@bot.message_handler(func=lambda m: m.content_type ==
                     'text' and m.text in ['INFO', 'ИНФОРМАЦИЯ', 'BİLGİ'])
@bot.message_handler(commands=['info'])
def command_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            responses['info'][
                lang(cid)].format(bot_username),
            reply_markup=markup,
            disable_web_page_preview=True)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
