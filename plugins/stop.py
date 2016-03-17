# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stop.py importado.{/cyan}'))


@bot.message_handler(commands=['stop'])
def command_stop(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_user(cid):
        # try:
        #     botan.track(
        #         botan_token,
        #         cid,
        #         to_json(m),
        #         "/stop"
        #     )
        # except:
        #     pass
        try:
            send_udp('stop')
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
        #bot.send_sticker(cid, open('amumu.webp','rb'))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['stop'][lang(cid)])
        # users.pop(str(cid))
        # Enviar sticker de Amumu llorando
        # with open('usuarios.json', 'w') as f:
        #     json.dump(users, f)
        db.usuarios.remove(str(cid))
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
