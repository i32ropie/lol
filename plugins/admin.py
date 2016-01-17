# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  admin.py importado.{/cyan}'))


@bot.message_handler(commands=['admin'])
def command_admin(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/admin"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = """
Comandos de administración

/all - Difundido a TODOS.
/all\_es _<mensaje>_ - Difundido a chats españoles.
/all\_en _<mensaje>_- Difundido a chats *NO* españoles.
/ban _<id>_ - Banea un ID.
/unban _<id>_ - Desbanea un ID.
/mute - No responder a baneados.
/unmute - Responder a baneados.
/msg _<id>_ _<mensaje>_ - Envia un mensaje a un ID.
/patch\_XX - Actualizar parche.
/ping - Comprobar si el bot está activo.
/reload - Reiniciar el bot.
/stats - Información de usuarios del bot.
/update\_champs - Actualizar base de datos de campeones.
/update\_rotation\_pic - Actualizar imagen de rotación gratuita.
/update\_rotation\_text - Actualizar texto de rotación gratuita.
/update\_sale\_pic - Actualizar imagen de ofertas.
/update\_sale\_text - Actualizar texto de ofertas.
"""
        bot.send_message(cid, txt, parse_mode="Markdown")
