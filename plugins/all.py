# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  all.py importado.{/cyan}'))


@bot.message_handler(commands=['all_es'])
def command_all_es(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        to_json(m),
        "/all_es"
    )
    errors = dict()
    save = list()
    delete = list()
    aux = str()
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = ' '.join(m.text.split(' ')[1:])
        if not txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Error, mensaje vacío.")
        else:
            # userStep[0] = 'all'
            for x in [y for y in users if users[y]['notify']
                      and lang(y) == 'es' and not is_banned(y)]:
                try:
                    bot.send_chat_action(int(x), 'typing')
                    bot.send_message(int(x), txt)
                except Exception as e:
                    if e.result.status_code == 403:
                        delete.append(x)
                        users.pop(x)
                    else:
                        errors[x] = json.loads(e.result.text)
                else:
                    save.append(x)
            cont = 1
            aux = "Conservados:"
            for x in save:
                aux += "\n\t" + str(cont) + ') ' + x
                cont += 1
            aux += "\nEliminados:"
            cont = 1
            for x in delete:
                aux += "\n\t" + str(cont) + ') ' + x
                cont += 1
            with open('tmp.txt', 'w') as f:
                f.write(aux)
            bot.send_chat_action(cid, 'typing')
            bot.send_document(cid, open('tmp.txt', 'rt'))
            if len(errors) != 0:
                aux = "Hubo error en:\n"
                for x in errors:
                    aux += "\n" + x + "\n\terror_code: " + \
                        str(errors[x]['error_code']) + "\n\tdescription: " + errors[x]['description']
                with open('tmp.txt', 'w') as f:
                    f.write(aux)
                bot.send_document(cid, open('tmp.txt', 'rt'))
            # userStep[0] = 0


@bot.message_handler(commands=['all_en'])
def command_all_en(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        to_json(m),
        "/all_en"
    )
    errors = dict()
    save = list()
    delete = list()
    aux = str()
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = ' '.join(m.text.split(' ')[1:])
        if not txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, "Error, mensaje vacío.")
        else:
            # userStep[0] = 'all'
            for x in [y for y in users if users[y]['notify']
                      and lang(y) != 'es' and not is_banned(y)]:
                try:
                    bot.send_chat_action(int(x), 'typing')
                    bot.send_message(int(x), txt)
                except Exception as e:
                    if e.result.status_code == 403:
                        delete.append(x)
                        users.pop(x)
                    else:
                        errors[x] = json.loads(e.result.text)
                else:
                    save.append(x)
            cont = 1
            aux = "Conservados:"
            for x in save:
                aux += "\n\t" + str(cont) + ') ' + x
                cont += 1
            aux += "\nEliminados:"
            cont = 1
            for x in delete:
                aux += "\n\t" + str(cont) + ') ' + x
                cont += 1
            with open('tmp.txt', 'w') as f:
                f.write(aux)
            bot.send_chat_action(cid, 'typing')
            bot.send_document(cid, open('tmp.txt', 'rt'))
            if len(errors) != 0:
                aux = "Hubo error en:\n"
                for x in errors:
                    aux += "\n" + x + "\n\terror_code: " + \
                        str(errors[x]['error_code']) + "\n\tdescription: " + errors[x]['description']
                with open('tmp.txt', 'w') as f:
                    f.write(aux)
                bot.send_document(cid, open('tmp.txt', 'rt'))
            # userStep[0] = 0


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
