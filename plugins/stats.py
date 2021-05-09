# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stats.py importado.{/cyan}'))


@bot.message_handler(commands=['stats'])
def command_usuarios(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        users = {
            'total': db.users.find().count(),
            'active': db.users.find({'active':True}).count(),
            'groups': {
                'total': db.users.find({'active':True, '_id':{'$regex':'^-'}}).count(),
                'detailed': {
                    'Spanish': db.users.find({'active':True, 'lang': 'es', '_id':{'$regex':'^-'}}).count(),
                    'English': db.users.find({'active':True, 'lang': 'en', '_id':{'$regex':'^-'}}).count(),
                    'Italian': db.users.find({'active':True, 'lang': 'it', '_id':{'$regex':'^-'}}).count(),
                    'German': db.users.find({'active':True, 'lang': 'de', '_id':{'$regex':'^-'}}).count(),
                    'Portuguese': db.users.find({'active':True, 'lang': 'pt', '_id':{'$regex':'^-'}}).count(),
                    'French': db.users.find({'active':True, 'lang': 'fr', '_id':{'$regex':'^-'}}).count(),
                    'Persian': db.users.find({'active':True, 'lang': 'fa', '_id':{'$regex':'^-'}}).count(),
                    'Polish': db.users.find({'active':True, 'lang': 'pl', '_id':{'$regex':'^-'}}).count(),
                    'Turkish': db.users.find({'active':True, 'lang': 'tr', '_id':{'$regex':'^-'}}).count(),
                    'Romanian': db.users.find({'active':True, 'lang': 'ro', '_id':{'$regex':'^-'}}).count(),
                    'Russian': db.users.find({'active':True, 'lang': 'ru', '_id':{'$regex':'^-'}}).count(),
                    'Arab': db.users.find({'active':True, 'lang': 'ar', '_id':{'$regex':'^-'}}).count()
                }
            },
            'privates': {
                'total': db.users.find({'active':True, '_id':{'$regex':'^[^-]'}}).count(),
                'detailed': {
                    'Spanish': db.users.find({'active':True, 'lang': 'es', '_id':{'$regex':'^[^-]'}}).count(),
                    'English': db.users.find({'active':True, 'lang': 'en', '_id':{'$regex':'^[^-]'}}).count(),
                    'Italian': db.users.find({'active':True, 'lang': 'it', '_id':{'$regex':'^[^-]'}}).count(),
                    'German': db.users.find({'active':True, 'lang': 'de', '_id':{'$regex':'^[^-]'}}).count(),
                    'Portuguese': db.users.find({'active':True, 'lang': 'pt', '_id':{'$regex':'^[^-]'}}).count(),
                    'French': db.users.find({'active':True, 'lang': 'fr', '_id':{'$regex':'^[^-]'}}).count(),
                    'Persian': db.users.find({'active':True, 'lang': 'fa', '_id':{'$regex':'^[^-]'}}).count(),
                    'Polish': db.users.find({'active':True, 'lang': 'pl', '_id':{'$regex':'^[^-]'}}).count(),
                    'Turkish': db.users.find({'active':True, 'lang': 'tr', '_id':{'$regex':'^[^-]'}}).count(),
                    'Romanian': db.users.find({'active':True, 'lang': 'ro', '_id':{'$regex':'^[^-]'}}).count(),
                    'Russian': db.users.find({'active':True, 'lang': 'ru', '_id':{'$regex':'^[^-]'}}).count(),
                    'Arab': db.users.find({'active':True, 'lang': 'ar', '_id':{'$regex':'^[^-]'}}).count()
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
