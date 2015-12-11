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
        if lang(cid) == 'es':
            lan = 'es'
        else:
            lan = 'en'
        with open('extra_data/changelog_' + lan+ '.txt', 'rt') as f:
            changelog = f.read()
        bot.send_message( cid, changelog, parse_mode="Markdown")
    else:
        bot.send_message( cid, responses['not_user'])
