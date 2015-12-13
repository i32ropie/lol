# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  all.py importado.{/cyan}'))

@bot.message_handler(commands=['all'])
def command_all(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['all'], reply_markup=types.ForceReply() )
        userStep[cid] = 'all'

@bot.message_handler(commands=['all_es'])
def command_all_es(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    aux = str()
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = ' '.join(m.text.split(' ')[1:])
        if not txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, "Error, mensaje vacío.")
        else:
            for x in users:
                if users[str(x)]['notify'] and not is_banned(x) and lang(x) == 'es':
                    try:
                        bot.send_chat_action( int(uid), 'typing')
                        bot.send_message( int(x), txt)
                    except:
                        delete.append(x)
                        #users.pop(uid)
                    else:
                        save.append(x)
            cont = 1
            aux = "Conservados:"
            for x in save:
                aux += "\n\t" + str(cont) + ') '+ x
                cont += 1
            aux += "\nEliminados:"
            cont = 1
            for x in delete:
                users.pop(x)
                aux += "\n\t" + str(cont) + ') '+ x
                cont += 1
            with open('tmp.txt','w') as f:
                f.write(aux)
            bot.send_chat_action(cid, 'typing')
            bot.send_document( cid, open('tmp.txt' ,'rt'))

@bot.message_handler(commands=['all_en'])
def command_all_en(m):
    cid = m.chat.id
    uid = m.from_user.id
    save = list()
    delete = list()
    aux = str()
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = ' '.join(m.text.split(' ')[1:])
        if not txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message( cid, "Error, mensaje vacío.")
        else:
            for uid in users:
                if users[str(uid)]['notify'] and not is_banned(uid) and lang(uid) != 'es':
                    try:
                        bot.send_chat_action( int(uid), 'typing')
                        bot.send_message( int(uid), txt)
                    except:
                        delete.append(uid)
                        #users.pop(uid)
                    else:
                        save.append(uid)
            cont = 1
            aux = "Conservados:"
            for x in save:
                aux += "\n\t" + str(cont) + ') '+ x
                cont += 1
            aux += "\nEliminados:"
            cont = 1
            for x in delete:
                users.pop(x)
                aux += "\n\t" + str(cont) + ') '+ x
                cont += 1
            with open('tmp.txt','w') as f:
                f.write(aux)
            bot.send_chat_action(cid, 'typing')
            bot.send_document( cid, open('tmp.txt' ,'rt'))
