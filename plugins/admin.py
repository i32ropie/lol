# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  admin.py importado.{/cyan}'))

@bot.message_handler(commands=['all'])
def command_all(m):
    cid = m.chat.id
    uid = m.from_user.id
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
/patch_es - Actualizar parche español.
/patch_en - Actualizar parche inglés.
/patch_it - Actualizar parche italiano.
/ping - Comprobar si el bot está activo.
/reload - Reiniciar el bot.
/update_rotation_pic - Actualizar imagen de rotación gratuita.
/update_rotation_text - Actualizar texto de rotación gratuita.
/update_sale_pic - Actualizar imagen de ofertas.
/update_sale_text - Actualizar texto de ofertas.
/stats - Información de usuarios del bot.
"""
        bot.send_message( cid, txt, parse_mode="Markdown")
