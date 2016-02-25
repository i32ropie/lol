# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  about.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'CRÉDITOS',
        'CREDITS',
        'CREDITI',
        'DANKSAGUNGEN',
        'CRÉDITS',
        'АВТОРЫ'])
@bot.message_handler(commands=['credits'])
def command_credits(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/credits"
        )
    except:
        pass
    url = botan.shorten_url(
        'https://github.com/eternnoir/pyTelegramBotAPI',
        botan_token,
        cid)
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
            cid, responses['about'][
                lang(cid)] % (url), parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
