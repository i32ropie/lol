# -*- coding: utf-8 -*-

from config import *
import platform, psutil, subprocess

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))

@bot.message_handler(commands=['system'])
def command_system(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        running = '\n*Running on*:\n'
        running += '\t🖥 {0}\n'.format(subprocess.getoutput('head -n1 /etc/issue | cut -d " " -f -3'))
        running += '\t💾 {0}\n'.format(subprocess.getoutput('uname -rs'))
        running += '\t💡 {0}\n'.format(subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | tr -s " " | cut -d " " -f 3-'))
        running += '\t🗃 {0}MB ({1}% used)\n'.format(int(psutil.virtual_memory()[0] / 1000 / 1000), psutil.virtual_memory()[2])
        running += '\t🐍 Python {0} ({1})\n'.format(str(platform.python_version()), str(platform.python_compiler()))
        running += '\t⌚️ {0}\n'.format(time.strftime("%c"))
        running += '\t⏱ {0}\n'.format(subprocess.getoutput('uptime -p'))
        bot.send_message( cid, running)
