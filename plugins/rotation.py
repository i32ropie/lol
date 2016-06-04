# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  rotation.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'ROTAÇÃO',
        'ROTACJA',
        'ФРИПИК',
        'ROTACIÓN',
        'ROTATION',
        'ROTAZIONE'])
@bot.message_handler(commands=['rotation'])
def command_rotation(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('rotation')
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
        txt = responses['rotation'][lang(cid)] + '\n'
        with open('extra_data/rotation.txt', 'rt') as f:
            txt += f.read()
        bot.send_chat_action(cid, 'typing')
        bot.send_photo(cid, extra['rotation'])
        bot.send_message(cid, txt)
    else:
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(commands=['update_rotation_text'])
def command_update_rotation(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_rotation_text')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_rotation_text_1'])
        userStep[cid] = 'update_rotation_text'


@bot.message_handler(commands=['update_rotation_pic'])
def command_update_pic(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_rotation_pic')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['update_rotation_pic_1'])
        userStep[cid] = 'update_rotation_pic'
