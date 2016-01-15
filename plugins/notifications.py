# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  notifications.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda message: message.text in [
        'NOTIFICAÇÕES',
        'NOTYFIKACJE',
        'NOTIFICATIONS',
        'NOTIFICACIONES',
        'NOTIFICHE',
        'BENACHRICHTIGUNGEN'])
@bot.message_handler(commands=['notify'])
def command_notify(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        json.dumps(to_json(m)),
        "/notify"
    )
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        if users[str(cid)]['notify']:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['notifications_1'][
                    lang(cid)], parse_mode="Markdown")
            users[str(cid)]['notify'] = False
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['notifications_2'][
                    lang(cid)], parse_mode="Markdown")
            users[str(cid)]['notify'] = True
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
