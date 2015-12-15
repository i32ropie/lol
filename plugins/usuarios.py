# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stats.py importado.{/cyan}'))

@bot.message_handler(commands=['stats'])
def command_usuarios(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        x = {'usuarios':{'total':0,'es':0,'en':0,'it':0,'de':0,'pl':0,'pt':0,'fr':0},'grupos':{'total':0,'es':0,'en':0,'it':0,'de':0,'pl':0,'pt':0,'fr':0}}
        for uid in users:
            if int(uid) > 0:
                x['usuarios']['total'] += 1
                x['usuarios'][lang(uid)] += 1
            else:
                x['grupos']['total'] += 1
                x['grupos'][lang(uid)] += 1
        txt = "*Usuarios*: " + str(x['usuarios']['total']) + "\n *-*Español: _" + str(x['usuarios']['es']) + "_\n *-*Inglés: _" \
        + str(x['usuarios']['en']) + "_\n *-*Italiano: _" + str(x['usuarios']['it']) + "_\n *-*Polaco: _" + str(x['usuarios']['pl'])\
        + "_\n *-*Francés: _" + str(x['usuarios']['fr']) + "_\n *-*Alemán: _" + str(x['usuarios']['de']) + "_\n *-*Portugués: _" + str(x['usuarios']['pt'])\
        + '\n\n*Grupos*: ' + str(x['grupos']['total']) + "\n *-*Español: _" + str(x['grupos']['es']) + "_\n *-*Inglés: _" \
        + str(x['grupos']['en']) + "_\n *-*Italiano: _" + str(x['grupos']['it']) + "_\n *-*Polaco: _" + str(x['grupos']['pl'])\
        + "_\n *-*Francés: _" + str(x['grupos']['fr']) + "_\n *-*Alemán: _" + str(x['grupos']['de']) + "_\n *-*Portugués: _" + str(x['grupos']['pt'])
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, txt, parse_mode="Markdown")
