# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  reload.py importado.{/cyan}'))


@bot.message_handler(commands=['reload'])
def command_reload(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        json.dumps(to_json(m)),
        "/reload"
    )
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['reload'], parse_mode="Markdown")
        print(Color(
            '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Reiniciando @League_of_Legends_bot{/cyan}'))
        exit()
