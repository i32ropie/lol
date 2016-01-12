# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stop.py importado.{/cyan}'))


@bot.message_handler(
    commands=['stop'], func=lambda msg: next_step_handler(0) == 0)
def command_stop(m):
    cid = m.chat.id
    if not is_recent(m):
        return None
    if is_user(cid):
        #bot.send_sticker(cid, open('amumu.webp','rb'))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['stop'][lang(cid)])
        users.pop(str(cid))
        # Enviar sticker de Amumu llorando
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
        for id in admins:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(id, "Usuario eliminado:\n\nNombre: " +
                             str(m.from_user.first_name) +
                             "\nAlias: @" +
                             str(m.from_user.username) +
                             "\nID: " +
                             str(cid))
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['stop_already_unuser'])
