# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  patch.py importado.{/cyan}'))


@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in [
                     'ATUALIZAÇÃO', 'ПАТЧ', 'PARCHE', 'PATCH', 'YAMA'])
@bot.message_handler(commands=['patch'])
def command_patch(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('patch')
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
        with open('extra_data/patch_' + lang(cid) + '.txt', 'rt') as f:
            patch = f.read()
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, patch, parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(
    commands=[
        'patch_es',
        'patch_en',
        'patch_it',
        'patch_pl',
        'patch_fr',
        'patch_de',
        'patch_ro',
        'patch_pt',
        'patch_fa',
        'patch_tr',
        'patch_ru',
        'patch_el'])
def command_update_patch(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp(m.text.lstrip('/').split(' ')[0].split('@')[0].lower())
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            "Envía el texto para actualizar *patch_" +
            m.text.split('_')[1] +
            ".txt* o escribe /cancel",
            parse_mode="Markdown")
        userStep[cid] = 'patch_' + m.text.split('_')[1]
