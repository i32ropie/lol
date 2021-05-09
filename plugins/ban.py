# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  ban.py importado.{/cyan}'))


@bot.message_handler(commands=['ban'])
def command_ban(m):
    cid = m.chat.id
    uid = m.from_user.id
    date = m.date
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
            if is_user(banned_id):
                if is_banned(banned_id):
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['ban']['failure'][1] %
                        banned_id)
                else:
                    db.users.update({"_id": banned_id},
                                       {"$set": {"banned": True}})
                    bot.send_chat_action(cid, 'typing')
                    bot.send_message(
                        cid, responses['ban']['success'] %
                        banned_id)
            else:
                # db.users.insert({
                #     "_id": banned_id,
                #     "lang": "en",
                #     "banned": True,
                #     "notify": True,
                #     "server": "",
                #     "summoner": ""
                # })
                db.users.insert({
                    "_id": banned_id,
                    "lang": "en",
                    "banned": True,
                    "notify": True,
                    "server": "",
                    "summoner": "",
                    "active": True,
                    "register": date,
                    "returns": []
                })
                bot.send_chat_action(cid, 'typing')
                bot.send_message(cid, responses['ban']['success'] % banned_id)


@bot.message_handler(commands=['unban'])
def command_unban(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        try:
            banned_id = m.text.split(' ')[1]
        except:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, responses['unban']['failure'][0])
            return None
        if isint(banned_id):
            if is_user(banned_id):
                if is_banned(banned_id):
                    db.users.update({"_id": banned_id},
                                       {"$set": {"banned": False}})
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
    if is_admin(uid):
        extra['muted'] = True
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Mensajes a baneados desactivados")
        with open("extra_data/extra.json", "w") as f:
            json.dump(extra, f)


@bot.message_handler(commands=['unmute'])
def command_unmute(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        extra['muted'] = False
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, "Mensajes a baneados activados")
        with open("extra_data/extra.json", "w") as f:
            json.dump(extra, f)
