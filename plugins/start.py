# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  start.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(
    types.KeyboardButton('ESPAÑOL'),
    types.KeyboardButton('ENGLISH'),
    types.KeyboardButton('ITALIANO'),
    types.KeyboardButton('POLSKI'),
    types.KeyboardButton('DEUTSCH'),
    types.KeyboardButton('FRANÇAIS'),
    types.KeyboardButton('PORTUGUÊS'),
    types.KeyboardButton('РУССКИЙ'),
    types.KeyboardButton('ROMÂNĂ'),
    # 'ไทย',
    # 'ΕΛΛΗΝΙΚΆ',
    types.KeyboardButton('PERSIAN'),
    types.KeyboardButton('TÜRKÇE'))


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if not is_user(cid):
        try:
            send_udp('start')
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
        try:
            idioma = m.from_user.language_code
        except:
            idioma = None
        if idioma in ['es','en','pt','pl','ro', 'fa']:
            db.usuarios.insert({
                "_id": str(cid),
                "lang": idioma,
                "banned": False,
                "notify": True,
                "server": "",
                "summoner": ""
            })
            for id in admins:
                bot.send_chat_action(cid, 'typing')
                bot.send_message(id, "Nuevo usuario\n\nNombre: " +
                                 str(m.from_user.first_name) +
                                 "\nAlias: @" +
                                 str(m.from_user.username) +
                                 "\nID: " +
                                 str(cid) +
                                 "\nIdioma: " +
                                 str(lang(cid)) +
                                 " (Autodetectado)")
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['start_autodetect'][
                    idioma])
            bot.send_message(
                cid, responses['start_2'][
                    idioma])
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid,
                responses['start_1'] %
                m.from_user.first_name,
                reply_markup=markup)
            userStep[cid] = 'start'
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['start_already_user'][lang(cid)])
