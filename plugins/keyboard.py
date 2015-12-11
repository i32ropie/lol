# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  keyboard.py importado.{/cyan}'))

markup_es = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_es.add( 'AYUDA', 'CONTACTO', 'INFORMACION')
markup_es.add( 'PARCHE', 'CHANGELOG', 'CALIFICAR')
markup_es.add( 'OFERTA', 'CAMPEONES', 'ROTACION')
markup_es.add( 'INVOCADOR', 'OCULTAR TECLADO' ,'PARTIDA')
markup_es.add( 'ASESINOS', 'LUCHADORES', 'TANQUES')
markup_es.add( 'APOYOS', 'MAGOS', 'TIRADORES')


markup_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_en.add( 'HELP', 'CONTACT', 'INFORMATION')
markup_en.add( 'PATCH', 'CHANGELOG', 'RATE')
markup_en.add( 'SALE', 'CHAMPIONS', 'ROTATION')
markup_en.add( 'SUMMONER', 'HIDE KEYBOARD', 'MATCH')
markup_en.add( 'ASSASSINS', 'FIGHTERS', 'TANKS')
markup_en.add( 'SUPPORTS', 'MAGES', 'ADCS')

markups = {
    "es": markup_es,
    "en": markup_en
}

@bot.message_handler(commands=['keyboard'])
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if cid > 0:
            bot.send_message( cid, responses['keyboard_1'][lang(cid)], reply_markup=markups[lang(cid)])
        else:
            bot.send_message( cid, responses['keyboard_2'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text=="OCULTAR TECLADO" or message.text=="HIDE KEYBOARD" )
@bot.message_handler(commands=['hideboard'])
def command_hideboard(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if cid > 0:
            bot.send_message( cid, responses['hideboard_1'][lang(cid)], reply_markup=types.ReplyKeyboardHide())
        else:
            bot.send_message( cid, responses['hideboard_2'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
