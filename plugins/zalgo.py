# -*- coding: utf-8 -*-

from config import *
import random

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  zalgo.py importado.{/cyan}'))

zalgo_up = [
    u'\u030d', u'\u030e', u'\u0304', u'\u0305',
    u'\u033f', u'\u0311', u'\u0306', u'\u0310',
    u'\u0352', u'\u0357', u'\u0351', u'\u0307',
    u'\u0308', u'\u030a', u'\u0342', u'\u0343',
    u'\u0344', u'\u034a', u'\u034b', u'\u034c',
    u'\u0303', u'\u0302', u'\u030c', u'\u0350',
    u'\u0300', u'\u0301', u'\u030b', u'\u030f',
    u'\u0312', u'\u0313', u'\u0314', u'\u033d',
    u'\u0309', u'\u0363', u'\u0364', u'\u0365',
    u'\u0366', u'\u0367', u'\u0368', u'\u0369',
    u'\u036a', u'\u036b', u'\u036c', u'\u036d',
    u'\u036e', u'\u036f', u'\u033e', u'\u035b',
    u'\u0346', u'\u031a']

zalgo_down = [
    u'\u0316', u'\u0317', u'\u0318', u'\u0319',
    u'\u031c', u'\u031d', u'\u031e', u'\u031f',
    u'\u0320', u'\u0324', u'\u0325', u'\u0326',
    u'\u0329', u'\u032a', u'\u032b', u'\u032c',
    u'\u032d', u'\u032e', u'\u032f', u'\u0330',
    u'\u0331', u'\u0332', u'\u0333', u'\u0339',
    u'\u033a', u'\u033b', u'\u033c', u'\u0345',
    u'\u0347', u'\u0348', u'\u0349', u'\u034d',
    u'\u034e', u'\u0353', u'\u0354', u'\u0355',
    u'\u0356', u'\u0359', u'\u035a', u'\u0323']

zalgo_mid = [
    u'\u0315', u'\u031b', u'\u0340', u'\u0341',
    u'\u0358', u'\u0321', u'\u0322', u'\u0327',
    u'\u0328', u'\u0334', u'\u0335', u'\u0336',
    u'\u034f', u'\u035c', u'\u035d', u'\u035e',
    u'\u035f', u'\u0360', u'\u0362', u'\u0338',
    u'\u0337', u'\u0361', u'\u0489']


@bot.message_handler(commands=['zalgo'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('zalgo')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        if len(m.text.split()) > 1:
            txt = m.text.split(None, 1)[1]
            out = [
                letter +
                random.choice(zalgo_up) *
                random.randint(
                    1,
                    5) +
                random.choice(zalgo_down) *
                random.randint(
                    1,
                    5) +
                random.choice(zalgo_mid) *
                random.randint(
                    1,
                    5) for letter in txt]
            bot.reply_to(m, ''.join(out))
    else:
        bot.send_message(cid, responses['not_user'])
