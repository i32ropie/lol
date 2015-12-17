# -*- coding: utf-8 -*-

from config import *
import platform, psutil, subprocess
from datetime import timedelta

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))

@bot.message_handler(commands=['system'])
def command_system(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))[:-7]
        running = '\n*Running on*:\n'
        running += '\tSystem: {0}\n'.format(subprocess.getoutput('head -n1 /etc/issue | cut -d " " -f -3'))
        running += '\tKerne: {0}\n'.format(subprocess.getoutput('uname -rs'))
        running += '\tProcessor: {0}\n'.format(subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | tr -s " " | cut -d " " -f 3-'))
        running += '\tRAM: {0}MB ({1}% used)\n'.format(int(psutil.virtual_memory()[0] / 1000 / 1000), psutil.virtual_memory()[2])
        running += '\tPython: {0} ({1})\n'.format(str(platform.python_version()), str(platform.python_compiler()))
        running += '\tServer time: {0}\n'.format(time.strftime("%c"))
        running += '\tUptime: Server up for {0}\n'.format(uptime_string)
        bot.send_message( cid, running, parse_mode="Markdown")
