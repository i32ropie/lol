# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  all.py importado.{/cyan}'))


@bot.message_handler(commands=['all_es'])
def command_all_es(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/all_es"
        )
    except:
        pass
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 1:
            bot.send_message(cid, "Error, no hay nada para enviar.")
            return
        for x in [y for y in users if users[y]['notify']
                  and lang(y) == 'es' and not is_banned(y)]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), ' '.join(m.text.split()[1:]))
            except Exception as e:
                if e.result.status_code == 403:
                    delete.append(x)
                    users.pop(x)
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_en'])
def command_all_en(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/all_en"
        )
    except:
        pass
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 1:
            bot.send_message(cid, "Error, no hay nada para enviar.")
            return
        for x in [y for y in users if users[y]['notify']
                  and lang(y) != 'es' and not is_banned(y)]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), ' '.join(m.text.split()[1:]))
            except Exception as e:
                if e.result.status_code == 403:
                    delete.append(x)
                    users.pop(x)
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_s'])
def command_all_s(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/all_s"
        )
    except:
        pass
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        for x in [y for y in users if users[y]['notify']
                  and not is_banned(y)]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), responses['all_s'][lang(x)])
            except Exception as e:
                if e.result.status_code == 403:
                    delete.append(x)
                    users.pop(x)
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)


@bot.message_handler(commands=['all_r'])
def command_all_r(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/all_r"
        )
    except:
        pass
    save = list()
    delete = list()
    if not is_recent(m):
        return None
    if is_admin(uid):
        for x in [y for y in users if users[y]['notify']
                  and not is_banned(y)]:
            try:
                bot.send_chat_action(int(x), 'typing')
                bot.send_message(int(x), responses['all_r'][lang(x)])
            except Exception as e:
                if e.result.status_code == 403:
                    delete.append(x)
                    users.pop(x)
            else:
                save.append(x)
        aux = "Conservados: {}\nEliminados: {}".format(len(save), len(delete))
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, aux)
