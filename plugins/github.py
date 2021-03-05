# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  github.py importado.{/cyan}'))


@bot.message_handler(commands=['github'])
def command_github(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('github')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        pull_info = os.popen('git pull').read()
        bot.send_message(cid, pull_info)
        if not pull_info.startswith('Already'):
            restart_process()
