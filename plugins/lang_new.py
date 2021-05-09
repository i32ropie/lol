# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  lang_new.py importado.{/cyan}'))

markup = telebot.types.InlineKeyboardMarkup()
markup.add(telebot.types.InlineKeyboardButton('ESPAÑOL', callback_data='lang es'),
        telebot.types.InlineKeyboardButton('ENGLISH', callback_data='lang en'),
        telebot.types.InlineKeyboardButton('ITALIANO', callback_data='lang it'))
markup.add(telebot.types.InlineKeyboardButton('POLSKI', callback_data='lang pl'),
        telebot.types.InlineKeyboardButton('DEUTSCH', callback_data='lang de'),
        telebot.types.InlineKeyboardButton('FRANÇAIS', callback_data='lang fr'))
markup.add(telebot.types.InlineKeyboardButton('PORTUGUÊS', callback_data='lang pt'),
        telebot.types.InlineKeyboardButton('РУССКИЙ', callback_data='lang ru'),
        telebot.types.InlineKeyboardButton('PERSIAN', callback_data='lang fa'))
markup.add(telebot.types.InlineKeyboardButton('TÜRKÇE', callback_data='lang tr'),
        telebot.types.InlineKeyboardButton('ROMÂNĂ', callback_data='lang ro'),
        telebot.types.InlineKeyboardButton('ARABIC', callback_data='lang ar'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'JĘZYK',
        'IDIOMA',
        'ЯЗЫК',
        'LIMBĂ',
        'LANGUAGE',
        'LINGUA',
        'SPRACHE',
        'LANGUE',
        'DİL'])
@bot.message_handler(commands=['lang_new'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        # Mandar mensaje con teclado
        bot.send_message(cid, "Selecciona un idioma", reply_markup=markup)
    else:
        bot.send_message(cid, responses['not_user'])


@bot.callback_query_handler(func=lambda call: call.data.startswith('lang'))
def callback_lang(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    user_lang = call.data.split(' ')[-1]
    db.users.update(
        {"_id": str(cid)},
        {"$set": {"lang": user_lang}}
    )
    bot.edit_message_text(responses['lang_2'][user_lang], cid, mid, reply_markup=markup)
