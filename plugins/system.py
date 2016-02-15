# -*- coding: utf-8 -*-

from config import *
import platform
import psutil
import subprocess

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))


@bot.message_handler(commands=['system'])
def command_system(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/system"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        running = '\n*Running on*:\n'
        running += '\t*System*: {0}\n'.format(
            subprocess.getoutput('head -n1 /etc/issue | cut -d " " -f -3'))
        running += '\t*Kernel*: {0}\n'.format(
            subprocess.getoutput('uname -rs'))
        running += '\t*Processor*: {0}\n'.format(subprocess.getoutput(
            'cat /proc/cpuinfo | grep "model name" | tr -s " " | cut -d " " -f 3-'))
        running += '\t*RAM*: {0}MB ({1}% used)\n'.format(
            int(psutil.virtual_memory()[0] / 1000 / 1000), psutil.virtual_memory()[2])
        running += '\t*Python*: {0} ({1})\n'.format(
            str(platform.python_version()), str(platform.python_compiler()))
        running += '\t*Server time*: {0}\n'.format(time.strftime("%c"))
        running += '\t*Uptime*: {}\n'.format(subprocess.getoutput('uptime -p'))
        bot.send_message(cid, running, parse_mode="Markdown")
