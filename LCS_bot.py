#!/usr/bin/env python3

#################################################
#                    IMPORTS                    #
#################################################
from colorclass import Color

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Cargando plugins...{/cyan}'))

from config import *
import importdir
import sys

#################################################
#                    BOT BODY                   #
#################################################

if sys.version_info.major < 3:
    raise Exception("Must be using Python 3")

importdir.do('plugins', globals())

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Plugins cargados.{/cyan}'))


try:
    bot.send_message(get_admin(), f"@{bot_username} ha sido encendido")
except Exception as e:
    bot.send_message(get_admin(), str(e))

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}@LoL_bot ha sido encendido.{/cyan}\n'))

#################################################
#                    POLLING                    #
#################################################

bot.polling()
