# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  all.py importado.{/cyan}'))


@bot.message_handler(commands=['all_es'])
def command_all_es(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 1:
            bot.send_message(cid, "Error, no hay nada para enviar.")
            return
        for x in [y['_id'] for y in db.users.find(
                {"notify": True, "lang": "es", "banned": False, "active": True})]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), ' '.join(m.text.split(' ')[1:]))
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        # db.users.remove(x)
                        db.users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_en'])
def command_all_en(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 1:
            bot.send_message(cid, "Error, no hay nada para enviar.")
            return
        for x in [y['_id'] for y in db.users.find(
                {"notify": True, "lang": {"$ne": "es"}, "banned": False, "active": True})]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), ' '.join(m.text.split(' ')[1:]))
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        # db.users.remove(x)
                        db.users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_s'])
def command_all_s(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        for x in [y['_id']
                  for y in db.users.find({"notify": True, "banned": False, "active": True})]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), responses['all_s'][lang(x)])
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        # db.users.remove(x)
                        db.users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_r'])
def command_all_r(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        for x in [y['_id']
                  for y in db.users.find({"notify": True, "banned": False, "active": True})]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), responses['all_r'][lang(x)])
            except Exception as e:
                try:
                    if e.result.status_code == 403:
                        delete.append(x)
                        # db.users.remove(x)
                        db.users.update({"_id": x}, {"$set": {"active": False}})
                except Exception as z:
                    bot.send_message(
                        52033876, send_exception(e), parse_mode="Markdown")
                    bot.send_message(
                        52033876, send_exception(z), parse_mode="Markdown")
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)
