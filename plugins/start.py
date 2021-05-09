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
    types.KeyboardButton('ARABIC'),
    types.KeyboardButton('TÜRKÇE'))


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    uid = m.from_user.id
    date = m.date
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if not is_user(cid):
        try:
            lang1, lang2 = m.from_user.language_code[
                :2], m.from_user.language_code
        except:
            lang1, lang2 = None, None
        if lang1 in [
            'es',
            'en',
            'pt',
            'pl',
            'ro',
            'fa',
            'it',
            'de',
            'tr',
            'fr',
            'ru',
            'ar']:
            if was_user(cid):
                db.users.update({"_id": str(cid)}, {"$set": {"active": True}})
                db.users.update({"_id": str(cid)}, {"$push": {"returns": date}})
                db.users.update({"_id": str(cid)}, {"$set": {"lang": lang1}})
                db.users.update({"_id": str(cid)}, {"$set": {"notify": True}})
            else:
                db.users.insert({
                    "_id": str(cid),
                    "lang": lang1,
                    "banned": False,
                    "notify": True,
                    "server": "",
                    "summoner": "",
                    "active": True,
                    "register": date,
                    "returns": []
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
                                 "\nDetectado: " +
                                 str(lang2))
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['start_autodetect'][
                    lang1])
            bot.send_message(
                cid, responses['start_2'][
                    lang1])
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
