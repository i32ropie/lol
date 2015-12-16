# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  keyboard.py importado.{/cyan}'))

markup_es = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_es.add( 'AYUDA', 'CONTACTO', 'INFO')
markup_es.add( 'PARCHE', 'CHANGELOG', 'CALIFICAR')
markup_es.add( 'OFERTA', 'CAMPEONES', 'ROTACION')
markup_es.add( 'INVOCADOR', 'OCULTAR TECLADO' ,'PARTIDA')
markup_es.add( 'POSICIONES', 'NOTIFICACIONES', 'CRÉDITOS')
markup_es.add( 'IDIOMA')

markup_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_en.add( 'HELP', 'CONTACT', 'INFO')
markup_en.add( 'PATCH', 'CHANGELOG', 'RATE')
markup_en.add( 'SALE', 'CHAMPIONS', 'ROTATION')
markup_en.add( 'SUMMONER', 'HIDE KEYBOARD', 'MATCH')
markup_en.add( 'ROLES', 'NOTIFICATIONS', 'CREDITS')
markup_en.add( 'LANGUAGE')

markup_it = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_it.add( 'AIUTO', 'CONTATTO', 'INFO')
markup_it.add( 'PATCH', 'CHANGELOG', 'QUALIFICARE')
markup_it.add( 'OFFERTA', 'CAMPIONI', 'ROTAZIONE')
markup_it.add( 'EVOCATORE', 'NASCONDI TASTIERA' ,'PARTITA')
markup_it.add( 'ROULI', 'NOTIFICHE', 'CREDITI')
markup_it.add( 'LINGUA')

markup_de = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_de.add( 'HILFE', 'KONTAKT', 'INFO')
markup_de.add( 'PATCH', 'ÄNDERUNGSPROTOKOLL', 'SIEGESRATE')
markup_de.add( 'ANGEBOTE', 'CHAMPIONS', 'ROTATION')
markup_de.add( 'BESCHWÖRER', 'VERBERGE TASTATUR', 'SPIEL')
markup_de.add( 'ROLLEN', 'BENACHRICHTIGUNGEN', 'DANKSAGUNGEN')
markup_de.add( 'SPRACHE')

markup_fr = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_fr.add( 'AIDE', 'CONTACT', 'INFO')
markup_fr.add( 'PATCH', 'CHANGELOG', 'NOTER')
markup_fr.add( 'VENTE', 'CHAMPIONS', 'ROTATION')
markup_fr.add( 'INVOCATEUR', 'CACHER CLAVIER', 'PARTIE')
markup_fr.add( 'RÔLES', 'NOTIFICATIONS', 'CRÉDITS')
markup_fr.add( 'LANGUE')

markup_pl, markup_fa = markup_en, markup_en

markups = {
    "es": markup_es,
    "en": markup_en,
    "it": markup_it,
    "pl": markup_pl,
    "fr": markup_fr,
    "de": markup_de,
    "fa": markup_fa
}

@bot.message_handler(commands=['keyboard'])
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, responses['keyboard_1'][lang(cid)], reply_markup=markups[lang(cid)])
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, responses['keyboard_2'][lang(cid)])
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['not_user'])

@bot.message_handler( func=lambda message: message.text in ["OCULTAR TECLADO","HIDE KEYBOARD","NASCONDI TASTIERA","VERBERGE TASTATUR","CACHER CLAVIER"])
@bot.message_handler(commands=['hideboard'])
def command_hideboard(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['hideboard_1'][lang(cid)], reply_markup=types.ReplyKeyboardHide())
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['not_user'])
