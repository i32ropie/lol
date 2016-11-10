# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  mine.py importado.{/cyan}'))


@bot.message_handler(commands=['mine'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('mine')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        if cid in [52033876, 4279004]:
            parametro = m.text.split(' ')[1] if len(m.text.split(' ')) > 1 else None
            tmp = int(os.popen('ps aux | grep java | wc -l').read())
            if not parametro:
                if tmp == 3:
                    bot.send_message(cid, "Servidor de minecraft encendido.")
                elif tmp == 2:
                    bot.send_message(cid, "Servidor de minecraft apagado.")
                else:
                    bot.send_message(52033876, "@Edurolp mira el server del minecraft que algo le pasa. tmp = {}".format(tmp))
            else:
                if parametro == 'start':
                    if tmp == 2:
                        bot.send_message(cid, "Iniciando servidor.")
                        os.popen('pm2 start 8')
                    else:
                        bot.send_message(cid, "Se supone que el server ya está encendido, avisa a @Edurolp si no funciona.")
                if parametro == 'stop':
                    if tmp > 2:
                        bot.send_message(cid, "Apagando servidor.")
                        os.popen('pm2 stop 8')
                    else:
                        bot.semd_message(cid, "El servidor ya estaba apagado.")
    else:
        bot.send_message(cid, responses['not_user'])
