# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  .py importado.{/cyan}'))


@bot.message_handler(func=lambda message: message.text ==
                     "ESPAÑOL" or message.text == "INGLES")
@bot.message_handler(commands=['comando'])
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
        # Comando
    else:
        bot.send_message(cid, responses['not_user'])
