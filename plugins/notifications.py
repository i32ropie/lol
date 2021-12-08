# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  notifications.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'NOTIFICAÇÕES',
        'NOTYFIKACJE',
        'NOTIFICATIONS',
        'NOTIFICĂRI',
        'NOTIFICACIONES',
        'NOTIFICHE',
        'УВЕДОМЛЕНИЯ',
        'BENACHRICHTIGUNGEN',
        'BİLDİRİMLER'])
@bot.message_handler(commands=['notify'])
def command_notify(m):
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
        if db.users.find_one(str(cid))['notify']:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['notifications_1'][
                    lang(cid)], parse_mode="Markdown")
            db.users.update_one(
                {"_id": str(cid)},
                {"$set": {"notify": False}})
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['notifications_2'][
                    lang(cid)], parse_mode="Markdown")
            db.users.update_one(
                {"_id": str(cid)},
                {"$set": {"notify": True}})
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
