# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  msg.py importado.{/cyan}'))


@bot.message_handler(commands=['msg'])
def command_msg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split(' ')) >= 3:
            if isint(m.text.split(' ')[1]):
                if is_user(m.text.split(' ')[1]):
                    try:
                        bot.send_message(
                            m.text.split(' ')[1], ' '.join(
                                m.text.split(' ')[
                                    2:]))
                    except:
                        bot.send_message(
                            cid, "Error. No se pudo enviar mensaje, quizá ya no es usuario.")
                    else:
                        bot.send_message(
                            cid, "Éxito. Mensaje enviado satisfactoriamente.")
                else:
                    bot.send_message(
                        cid, "Error. El usuario no se encuentra en la base de datos.")
            else:
                bot.send_message(
                    cid, "Error. Debes introducir un número como ID.")
        else:
            bot.send_message(
                cid,
                "Error. Debes introducir `/msg <ID> <Mensaje>`",
                parse_mode="Markdown")
