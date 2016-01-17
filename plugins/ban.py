# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  ban.py importado.{/cyan}'))


@bot.message_handler(commands=['ban'])
def command_ban(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/cancel"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        try:
            banned_id = m.text.split(' ')[1]
        except:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, responses['ban']['failure'][0])
            return None
        if isint(banned_id):
            if banned_id in users:
                if is_banned(banned_id):
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['ban']['failure'][1] %
                        banned_id)
                else:
                    users[str(banned_id)]['banned'] = True
                    with open('usuarios.json', 'w') as f:
                        json.dump(users, f)
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['ban']['success'] %
                        banned_id)
            else:
                users[
                    str(banned_id)] = {
                    "lang": "en",
                    "banned": True,
                    "notify": True}
                with open('usuarios.json', 'w') as f:
                    json.dump(users, f)
                bot.send_chat_action(cid, 'typing')
                bot.send_message(cid, responses['ban']['success'] % banned_id)
                #bot.send_message( cid, responses['ban']['failure'][2]%banned_id)


@bot.message_handler(commands=['unban'])
def command_unban(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        to_json(m),
        "/unban"
    )
    if not is_recent(m):
        return None
    if is_admin(uid):
        try:
            banned_id = m.text.split(' ')[1]
        except:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, responses['unban']['failure'][0])
            return None
        if isint(banned_id):
            if banned_id in users:
                if is_banned(banned_id):
                    users[str(banned_id)]['banned'] = False
                    with open('usuarios.json', 'w') as f:
                        json.dump(users, f)
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['unban']['success'] %
                        banned_id)
                else:
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['unban']['failure'][1] %
                        banned_id)
            else:
                bot.send_chat_action(cid, 'typing')
                bot.send_message(
                    cid, responses['unban']['failure'][2] %
                    banned_id)


@bot.message_handler(commands=['mute'])
def command_mute(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        to_json(m),
        "/mute"
    )
    if is_admin(uid):
        extra['muted'] = True
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Mensajes a baneados desactivados")


@bot.message_handler(commands=['unmute'])
def command_unmute(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        to_json(m),
        "/unmute"
    )
    if is_admin(uid):
        extra['muted'] = False
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Mensajes a baneados activados")
