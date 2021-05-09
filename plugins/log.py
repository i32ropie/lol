# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  log.py importado.{/cyan}'))


@bot.message_handler(commands=['log'])
def command_log(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        if extra["log"]:
            extra["log"] = False
            bot.send_message(cid, "Log desactivado")
        else:
            extra["log"] = True
            bot.send_message(cid, "Log activado")
        with open("extra_data/extra.json", "w") as f:
            json.dump(extra, f)
