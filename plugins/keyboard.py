# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  keyboard.py importado.{/cyan}'))

markup_es = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_es.add(
    types.KeyboardButton('AYUDA'),
    types.KeyboardButton('CONTACTO'),
    types.KeyboardButton('INFO'))
markup_es.add(
    types.KeyboardButton('PARCHE'),
    types.KeyboardButton('IDIOMA'),
    types.KeyboardButton('CALIFICAR'))
markup_es.add(
    types.KeyboardButton('OFERTA'),
    types.KeyboardButton('CAMPEONES'),
    types.KeyboardButton('ROTACIÓN'))
markup_es.add(
    types.KeyboardButton('INVOCADOR'),
    types.KeyboardButton('OCULTAR TECLADO'),
    types.KeyboardButton('PARTIDA'))
markup_es.add(
    types.KeyboardButton('POSICIONES'),
    types.KeyboardButton('NOTIFICACIONES'),
    types.KeyboardButton('CRÉDITOS'))


markup_pt = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_pt.add(
    types.KeyboardButton('AJUDA'),
    types.KeyboardButton('CONTATO'),
    types.KeyboardButton('INFO'))
markup_pt.add(
    types.KeyboardButton('ATUALIZAÇÃO'),
    types.KeyboardButton('IDIOMA'),
    types.KeyboardButton('AVALIAR'))
markup_pt.add(
    types.KeyboardButton('PROMOÇÕES'),
    types.KeyboardButton('CAMPEÕES'),
    types.KeyboardButton('ROTAÇÃO'))
markup_pt.add(
    types.KeyboardButton('INVOCADOR'),
    types.KeyboardButton('ESCONDER TECLADO'),
    types.KeyboardButton('PARTIDA'))
markup_pt.add(
    types.KeyboardButton('PAPÉIS'),
    types.KeyboardButton('NOTIFICAÇÕES'),
    types.KeyboardButton('CRÉDITOS'))


markup_en = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_en.add(
    types.KeyboardButton('HELP'),
    types.KeyboardButton('CONTACT'),
    types.KeyboardButton('INFO'))
markup_en.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('LANGUAGE'),
    types.KeyboardButton('RATE'))
markup_en.add(
    types.KeyboardButton('SALE'),
    types.KeyboardButton('CHAMPIONS'),
    types.KeyboardButton('ROTATION'))
markup_en.add(
    types.KeyboardButton('SUMMONER'),
    types.KeyboardButton('HIDE KEYBOARD'),
    types.KeyboardButton('MATCH'))
markup_en.add(
    types.KeyboardButton('ROLES'),
    types.KeyboardButton('NOTIFICATIONS'),
    types.KeyboardButton('CREDITS'))


markup_ro = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_ro.add(
    types.KeyboardButton('AJUTOR'),
    types.KeyboardButton('CONTACT'),
    types.KeyboardButton('INFORMAȚII'))
markup_ro.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('LIMBĂ'),
    types.KeyboardButton('RATĂ'))
markup_ro.add(
    types.KeyboardButton('REDUCERI'),
    types.KeyboardButton('CAMPIONI'),
    types.KeyboardButton('ROTAȚIE'))
markup_ro.add(
    types.KeyboardButton('INVOCATOR'),
    types.KeyboardButton('ASCUNDE TASTATURA'),
    types.KeyboardButton('MECI'))
markup_ro.add(
    types.KeyboardButton('ROLURI'),
    types.KeyboardButton('NOTIFICĂRI'),
    types.KeyboardButton('CONTRIBUITORI'))


markup_it = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_it.add(
    types.KeyboardButton('AIUTO'),
    types.KeyboardButton('CONTATTO'),
    types.KeyboardButton('INFO'))
markup_it.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('LINGUA'),
    types.KeyboardButton('QUALIFICARE'))
markup_it.add(
    types.KeyboardButton('OFFERTA'),
    types.KeyboardButton('CAMPIONI'),
    types.KeyboardButton('ROTAZIONE'))
markup_it.add(
    types.KeyboardButton('EVOCATORE'),
    types.KeyboardButton('NASCONDI TASTIERA'),
    types.KeyboardButton('PARTITA'))
markup_it.add(
    types.KeyboardButton('RUOLI'),
    types.KeyboardButton('NOTIFICHE'),
    types.KeyboardButton('CREDITI'))


markup_de = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_de.add(
    types.KeyboardButton('HILFE'),
    types.KeyboardButton('KONTAKT'),
    types.KeyboardButton('INFO'))
markup_de.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('SPRACHE'),
    types.KeyboardButton('SIEGESRATE'))
markup_de.add(
    types.KeyboardButton('ANGEBOTE'),
    types.KeyboardButton('CHAMPIONS'),
    types.KeyboardButton('ROTATION'))
markup_de.add(
    types.KeyboardButton('BESCHWÖRER'),
    types.KeyboardButton('VERBERGE TASTATUR'),
    types.KeyboardButton('SPIEL'))
markup_de.add(types.KeyboardButton('ROLLEN'), types.KeyboardButton(
    'BENACHRICHTIGUNGEN'), types.KeyboardButton('DANKSAGUNGEN'))


markup_fr = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_fr.add(
    types.KeyboardButton('AIDE'),
    types.KeyboardButton('CONTACT'),
    types.KeyboardButton('INFO'))
markup_fr.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('LANGUE'),
    types.KeyboardButton('NOTER'))
markup_fr.add(
    types.KeyboardButton('VENTE'),
    types.KeyboardButton('CHAMPIONS'),
    types.KeyboardButton('ROTATION'))
markup_fr.add(
    types.KeyboardButton('INVOCATEUR'),
    types.KeyboardButton('CACHER CLAVIER'),
    types.KeyboardButton('PARTIE'))
markup_fr.add(
    types.KeyboardButton('RÔLES'),
    types.KeyboardButton('NOTIFICATIONS'),
    types.KeyboardButton('CRÉDITS'))


markup_pl = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_pl.add(
    types.KeyboardButton('POMOC'),
    types.KeyboardButton('KONTAKT'),
    types.KeyboardButton('INFO'))
markup_pl.add(
    types.KeyboardButton('PATCH'),
    types.KeyboardButton('JĘZYK'),
    types.KeyboardButton('KWALIFIKOWAĆ'))
markup_pl.add(
    types.KeyboardButton('WYPRZEDAŻ'),
    types.KeyboardButton('BOHATEROWIE'),
    types.KeyboardButton('ROTACJA'))
markup_pl.add(
    types.KeyboardButton('PRZYWOŁYWACZ'),
    types.KeyboardButton('UKRYJ KLAWIATURĘ'),
    types.KeyboardButton('MECZ'))
markup_pl.add(
    types.KeyboardButton('ROLE'),
    types.KeyboardButton('NOTYFIKACJE'),
    types.KeyboardButton('CREDITS'))


markup_th = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup_pl.add('', '', '')
# markup_pl.add('', '', '')
# markup_pl.add('', '', '')
# markup_pl.add('', '', '')
# markup_pl.add('', '', '')


markup_el = types.ReplyKeyboardMarkup(resize_keyboard=True)
# markup_el.add('', '', '')
# markup_el.add('', '', '')
# markup_el.add('', '', '')
# markup_el.add('', '', '')
# markup_el.add('', '', '')


markup_tr = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_tr.add(
    types.KeyboardButton('YARDIM'),
    types.KeyboardButton('İLETİŞİM'),
    types.KeyboardButton('BİLGİ'))
markup_tr.add(
    types.KeyboardButton('YAMA'),
    types.KeyboardButton('DİL'),
    types.KeyboardButton('DEĞER'))
markup_tr.add(
    types.KeyboardButton('SATIŞ'),
    types.KeyboardButton('ŞAMPİYONLAR'),
    types.KeyboardButton('ROTASYON'))
markup_tr.add(
    types.KeyboardButton('SİHİRDAR'),
    types.KeyboardButton('KLAVYEYİ GİZLE'),
    types.KeyboardButton('KARŞILAŞMA'))
markup_tr.add(
    types.KeyboardButton('ROLLER'),
    types.KeyboardButton('BİLDİRİMLER'),
    types.KeyboardButton('JENERİK'))


markup_ru = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_ru.add(
    types.KeyboardButton('ПОМОЩЬ'),
    types.KeyboardButton('КОНТАКТЫ'),
    types.KeyboardButton('ИНФОРМАЦИЯ'))
markup_ru.add(
    types.KeyboardButton('ПАТЧ'),
    types.KeyboardButton('ЯЗЫК'),
    types.KeyboardButton('ОТЗЫВ'))
markup_ru.add(
    types.KeyboardButton('РАСПРОДАЖА'),
    types.KeyboardButton('ЧЕМПИОНЫ'),
    types.KeyboardButton('ФРИПИК'))
markup_ru.add(
    types.KeyboardButton('ПРИЗЫВАТЕЛЬ'),
    types.KeyboardButton('СКРЫТЬ КЛАВИАТУРУ'),
    types.KeyboardButton('МАТЧ'))
markup_ru.add(
    types.KeyboardButton('РОЛИ'),
    types.KeyboardButton('УВЕДОМЛЕНИЯ'),
    types.KeyboardButton('АВТОРЫ'))


markup_fa = markup_ar = markup_en


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
    "ru": markup_ru,
    "tr": markup_tr,
    "ro": markup_ro,
    "ar": markup_ar
}


@bot.message_handler(commands=['keyboard'])
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('keyboard')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
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
        "CACHER CLAVIER",
        "ASCUNDE TASTATURA",
        "KLAVYEYİ GİZLE"])
@bot.message_handler(commands=['hideboard'])
def command_hideboard(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('hideboard')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
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
            reply_markup=types.ReplyKeyboardRemove(selective=False))
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
