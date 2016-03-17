# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  keyboard.py importado.{/cyan}'))

markup_es = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_es.add('AYUDA', 'CONTACTO', 'INFO')
markup_es.add('PARCHE', 'IDIOMA', 'CALIFICAR')
markup_es.add('OFERTA', 'CAMPEONES', 'ROTACIÓN')
markup_es.add('INVOCADOR', 'OCULTAR TECLADO', 'PARTIDA')
markup_es.add('POSICIONES', 'NOTIFICACIONES', 'CRÉDITOS')


markup_pt = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_pt.add('AJUDA', 'CONTATO', 'INFO')
markup_pt.add('ATUALIZAÇÃO', 'IDIOMA', 'AVALIAR')
markup_pt.add('PROMOÇÕES', 'CAMPEÕES', 'ROTAÇÃO')
markup_pt.add('INVOCADOR', 'ESCONDER TECLADO', 'PARTIDA')
markup_pt.add('PAPÉIS', 'NOTIFICAÇÕES', 'CRÉDITOS')


markup_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_en.add('HELP', 'CONTACT', 'INFO')
markup_en.add('PATCH', 'LANGUAGE', 'RATE')
markup_en.add('SALE', 'CHAMPIONS', 'ROTATION')
markup_en.add('SUMMONER', 'HIDE KEYBOARD', 'MATCH')
markup_en.add('ROLES', 'NOTIFICATIONS', 'CREDITS')


markup_it = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_it.add('AIUTO', 'CONTATTO', 'INFO')
markup_it.add('PATCH', 'LINGUA', 'QUALIFICARE')
markup_it.add('OFFERTA', 'CAMPIONI', 'ROTAZIONE')
markup_it.add('EVOCATORE', 'NASCONDI TASTIERA', 'PARTITA')
markup_it.add('RUOLI', 'NOTIFICHE', 'CREDITI')


markup_de = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_de.add('HILFE', 'KONTAKT', 'INFO')
markup_de.add('PATCH', 'SPRACHE', 'SIEGESRATE')
markup_de.add('ANGEBOTE', 'CHAMPIONS', 'ROTATION')
markup_de.add('BESCHWÖRER', 'VERBERGE TASTATUR', 'SPIEL')
markup_de.add('ROLLEN', 'BENACHRICHTIGUNGEN', 'DANKSAGUNGEN')


markup_fr = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_fr.add('AIDE', 'CONTACT', 'INFO')
markup_fr.add('PATCH', 'LANGUE', 'NOTER')
markup_fr.add('VENTE', 'CHAMPIONS', 'ROTATION')
markup_fr.add('INVOCATEUR', 'CACHER CLAVIER', 'PARTIE')
markup_fr.add('RÔLES', 'NOTIFICATIONS', 'CRÉDITS')
markup_fr.add('')

markup_pl = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_pl.add('POMOC', 'KONTAKT', 'INFO')
markup_pl.add('PATCH', 'JĘZYK', 'KWALIFIKOWAĆ')
markup_pl.add('WYPRZEDAŻ', 'BOHATEROWIE', 'ROTACJA')
markup_pl.add('PRZYWOŁYWACZ', 'UKRYJ KLAWIATURĘ', 'MECZ')
markup_pl.add('ROLE', 'NOTYFIKACJE', 'CREDITS')


markup_th = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_pl.add('', '', '')
markup_pl.add('', '', '')
markup_pl.add('', '', '')
markup_pl.add('', '', '')
markup_pl.add('', '', '')


markup_el = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_el.add('', '', '')
markup_el.add('', '', '')
markup_el.add('', '', '')
markup_el.add('', '', '')
markup_el.add('', '', '')


markup_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_ru.add('ПОМОЩЬ', 'КОНТАКТЫ', 'ИНФОРМАЦИЯ')
markup_ru.add('ПАТЧ', 'ЯЗЫК', 'ОТЗЫВ')
markup_ru.add('РАСПРОДАЖА', 'ЧЕМПИОНЫ', 'ФРИПИК')
markup_ru.add('ПРИЗЫВАТЕЛЬ', 'СКРЫТЬ КЛАВИАТУРУ', 'МАТЧ')
markup_ru.add('РОЛИ', 'УВЕДОМЛЕНИЯ', 'АВТОРЫ')


markup_fa = markup_en


markups = {
    "es": markup_es,
    "en": markup_en,
    "it": markup_it,
    "pl": markup_pl,
    "fr": markup_fr,
    "pt": markup_pt,
    "de": markup_de,
    "fa": markup_fa,
    "th": markup_th,
    "el": markup_el,
    "ru": markup_ru
}


@bot.message_handler(commands=['keyboard'])
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/keyboard"
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
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['keyboard_1'][
                    lang(cid)], reply_markup=markups[
                    lang(cid)])
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, responses['keyboard_2'][lang(cid)])
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        "ESCONDER TECLADO",
        "UKRYJ KLAWIATURĘ",
        "OCULTAR TECLADO",
        "HIDE KEYBOARD",
        "СКРЫТЬ КЛАВИАТУРУ",
        "NASCONDI TASTIERA",
        "VERBERGE TASTATUR",
        "CACHER CLAVIER"])
@bot.message_handler(commands=['hideboard'])
def command_hideboard(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/hideboard"
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
            cid,
            responses['hideboard_1'][
                lang(cid)],
            reply_markup=types.ReplyKeyboardHide())
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
