# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  res.py importado.{/cyan}'))


@bot.message_handler(
    commands=['res'],
    func=lambda m: m.reply_to_message and m.content_type == 'text' and len(
        m.text.split()) > 1)
def command_res(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('res')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if is_admin(cid):
        answer = m.text.split(None, 1)[1]
        parse_mode = "Markdown" if answer.startswith('!') else None
        m_text = m.reply_to_message.text.split('\n')
        m_id = m_text[5].split(': ')[1]
        c_id = m_text[6].split(': ')[1]
        try:
            bot.send_message(
                c_id,
                answer.lstrip('!'),
                parse_mode=parse_mode,
                reply_to_message_id=m_id)
        except Exception as e:
            bot.send_message(
                52033876,
                send_exception(e),
                parse_mode="Markdown")
