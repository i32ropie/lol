# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  filter.py importado.{/cyan}'))


@bot.message_handler(
    commands=['filter'],
    func=lambda m: m.content_type == 'text' and len(
        m.text.split()) == 2 and isint(
            m.text.split()[1]))
def command_filter(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('res')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if is_admin(cid):
        ID = int(m.text.split()[1])
        if ID not in filtered and is_user(ID):
            filtered.append(ID)
            bot.send_message(cid, "El chat {} será redirigido.".format(ID))
        elif ID in filtered:
            filtered.remove(ID)
            bot.send_message(
                cid, "El chat {} dejará de ser redirigido.".format(ID))
