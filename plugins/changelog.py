# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  changelog.py importado.{/cyan}'))

@bot.message_handler( content_types=['text'], func=lambda message: message.text=="CHANGELOG")
@bot.message_handler(commands=['changelog'])
def command_changelog(m):
    cid = m.chat.id
    uid = m.from_user.id
    aux = dict()
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        with open('extra_data/changelog_es.txt', 'rt') as f:
            aux['es'] = f.read()
        with open('extra_data/changelog_en.txt', 'rt') as f:
            aux['en'] = f.read()
        bot.send_message( cid, aux[lang(cid)], parse_mode="Markdown")
    else:
        bot.send_message( cid, responses['not_user'])
