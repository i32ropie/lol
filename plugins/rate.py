# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rate.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'AVALIAR',
        'KWALIFIKOWAĆ',
        'CALIFICAR',
        'RATE',
        'QUALIFICARE',
        'ОТЗЫВ',
        'SIEGESRATE',
        'NOTER'])
@bot.message_handler(commands=['rate'])
def command_rate(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('rate')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    url = 'https://telegram.me/storebot?start=league_of_legends_bot'
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['rate'][lang(cid)] % (url))
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
