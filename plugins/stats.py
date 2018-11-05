# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stats.py importado.{/cyan}'))


@bot.message_handler(commands=['stats'])
def command_usuarios(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('stats')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        users = {
            'total': db.usuarios.find().count(),
            'active': db.usuarios.find({'active':True}).count(),
            'groups': {
                'total': db.usuarios.find({'active':True, '_id':{'$regex':'^-'}}).count(),
                'detailed': {
                    'es': db.usuarios.find({'active':True, 'lang': 'es', '_id':{'$regex':'^-'}}).count(),
                    'en': db.usuarios.find({'active':True, 'lang': 'en', '_id':{'$regex':'^-'}}).count(),
                    'it': db.usuarios.find({'active':True, 'lang': 'it', '_id':{'$regex':'^-'}}).count(),
                    'de': db.usuarios.find({'active':True, 'lang': 'de', '_id':{'$regex':'^-'}}).count(),
                    'pt': db.usuarios.find({'active':True, 'lang': 'pt', '_id':{'$regex':'^-'}}).count(),
                    'fr': db.usuarios.find({'active':True, 'lang': 'fr', '_id':{'$regex':'^-'}}).count(),
                    'fa': db.usuarios.find({'active':True, 'lang': 'fa', '_id':{'$regex':'^-'}}).count(),
                    'pl': db.usuarios.find({'active':True, 'lang': 'pl', '_id':{'$regex':'^-'}}).count(),
                    'tr': db.usuarios.find({'active':True, 'lang': 'tr', '_id':{'$regex':'^-'}}).count(),
                    'ro': db.usuarios.find({'active':True, 'lang': 'ro', '_id':{'$regex':'^-'}}).count(),
                    'ru': db.usuarios.find({'active':True, 'lang': 'ru', '_id':{'$regex':'^-'}}).count(),
                    'ar': db.usuarios.find({'active':True, 'lang': 'ar', '_id':{'$regex':'^-'}}).count()
                }
            },
            'privates': {
                'total': db.usuarios.find({'active':True, '_id':{'$regex':'^[^-]'}}).count(),
                'detailed': {
                    'es': db.usuarios.find({'active':True, 'lang': 'es', '_id':{'$regex':'^[^-]'}}).count(),
                    'en': db.usuarios.find({'active':True, 'lang': 'en', '_id':{'$regex':'^[^-]'}}).count(),
                    'it': db.usuarios.find({'active':True, 'lang': 'it', '_id':{'$regex':'^[^-]'}}).count(),
                    'de': db.usuarios.find({'active':True, 'lang': 'de', '_id':{'$regex':'^[^-]'}}).count(),
                    'pt': db.usuarios.find({'active':True, 'lang': 'pt', '_id':{'$regex':'^[^-]'}}).count(),
                    'fr': db.usuarios.find({'active':True, 'lang': 'fr', '_id':{'$regex':'^[^-]'}}).count(),
                    'fa': db.usuarios.find({'active':True, 'lang': 'fa', '_id':{'$regex':'^[^-]'}}).count(),
                    'pl': db.usuarios.find({'active':True, 'lang': 'pl', '_id':{'$regex':'^[^-]'}}).count(),
                    'tr': db.usuarios.find({'active':True, 'lang': 'tr', '_id':{'$regex':'^[^-]'}}).count(),
                    'ro': db.usuarios.find({'active':True, 'lang': 'ro', '_id':{'$regex':'^[^-]'}}).count(),
                    'ru': db.usuarios.find({'active':True, 'lang': 'ru', '_id':{'$regex':'^[^-]'}}).count(),
                    'ar': db.usuarios.find({'active':True, 'lang': 'ar', '_id':{'$regex':'^[^-]'}}).count()
                }
            }            
        }
        text = "*Total*: _{}_\n*Active*: _{}_\n\n*Group chats*: _{}_\n\t- {}\n\n*Private chats*: _{}_\n\t- {}".format(
            users['total'],
            users['active'],
            users['groups']['total'],
            '\n\t- '.join(['*{}*: _{}_'.format(x[0], x[1]) for x in sorted(users['groups']['detailed'].items(), key=lambda x: x[1], reverse=True)]),
            users['privates']['total'],
            '\n\t- '.join(['*{}*: _{}_'.format(x[0], x[1]) for x in sorted(users['privates']['detailed'].items(), key=lambda x: x[1], reverse=True)])
        )
        bot.send_message(cid, text, parse_mode="Markdown")
    else:
        bot.send_message(cid, responses['not_user'])
