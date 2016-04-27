# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  media.py importado.{/cyan}'))


@bot.message_handler(commands=['media'])
def command_media(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('media')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 2:
            if isint(m.text.split(' ')[1]):
                if m.reply_to_message:
                    try:
                        bot.forward_message(int(m.text.split()[1]), m.reply_to_message.chat.id, m.reply_to_message.message_id)
                    except:
                        bot.send_message(cid, "Error envíando a " + m.text.split()[1])
                else:
                    bot.send_message(cid, "Error, debes responder a un mensaje.")
            else:
                bot.send_message(cid, "Error, el argumento debe ser un número entero.")
        else:
            bot.send_message(cid, "Error, la sintaxis del comando es:\n/media _<id>_ - Reenvía al id el mensaje al que se le responde.", parse_mode="Markdown")
