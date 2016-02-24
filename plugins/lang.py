# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  lang.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(
    'ESPAÑOL',
    'ENGLISH',
    'ITALIANO',
    'POLSKI',
    'DEUTSCH',
    'FRANÇAIS',
    'PORTUGUÊS',
    'РУССКИЙ',
    'ไทย',
    'ΕΛΛΗΝΙΚΆ',
    'PERSIAN')


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'JĘZYK',
        'IDIOMA',
        'LANGUAGE',
        'LINGUA',
        'SPRACHE',
        'LANGUE'])
@bot.message_handler(commands=['lang'])
def command_lang(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/lang"
        )
    except:
        pass
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
            cid, responses['lang_1'][
                lang(cid)], reply_markup=markup)
        userStep[cid] = 'lang'
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
