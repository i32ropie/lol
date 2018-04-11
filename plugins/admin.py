# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  admin.py importado.{/cyan}'))


@bot.message_handler(commands=['admin'])
def command_admin(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('admin')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = """
Comandos de administración

/github - Comprueba si hay actualizaciones en github y reinicia el bot sin es necesario.
/all\_es _<mensaje>_ - Difundido a chats españoles.
/all\_en _<mensaje>_- Difundido a chats *NO* españoles.
/all\_s - Difundido de ofertas (Usar los jueves).
/all\_r - Difundido de ofertas+rotación (Usar los lunes).
/ban _<id>_ - Banea un ID.
/exec _<code>_ - Ejecuta el siguiente bloque de código.
/unban _<id>_ - Desbanea un ID.
/mute - No responder a baneados.
/unmute - Responder a baneados.
/msg _<id>_ _<mensaje>_ - Envia un mensaje a un ID.
/media _<id>_ - Reenvía al id el mensaje al que se le responde.
/patch\_XX - Actualizar parche.
/reload - Reiniciar el bot.
/res _[!]_- Usado respondiendo a un mensaje de contacto le responde. Empieza la respuesta por ! para usar Markdown.
/stats - Información de usuarios del bot.
/system - Información del servidor.
/update\_champs\_1 - Actualizar base de datos de campeones.
/update\_champs\_2 - Actualizar base de datos de campeones.
/update\_champs\_keys - Actualizar ese archivo.
/update\_rotation\_pic - Actualizar imagen de rotación gratuita.
/update\_rotation\_text - Actualizar texto de rotación gratuita.
/update\_sale\_pic - Actualizar imagen de ofertas.
/update\_sale\_text - Actualizar texto de ofertas.
"""
        bot.send_message(cid, txt, parse_mode="Markdown")
