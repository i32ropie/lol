# -*- coding: utf-8 -*-

from config import *
import requests


print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  me.py importado.{/cyan}'))


@bot.message_handler(commands=['me'])
def command_m(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        try:
            summoner = db.users.find_one(str(uid))['summoner']
            region = db.users.find_one(str(uid))['server']
        except:
            bot.send_message(cid, responses['me_error'][lang(cid)])
            return
        if summoner and region:
            res_text, res_info = get_summoner_info(
                    summoner,
                    region,
                    cid)
            if res_info:
                keyboard = types.InlineKeyboardMarkup()
                # if is_beta(cid):
                c_data = {
                    "r":region,
                    "s":summoner,
                    "a":"h"
                }
                keyboard.add(types.InlineKeyboardButton(responses['matches_history'][lang(cid)], callback_data=json.dumps(c_data)))

                keyboard.add(types.InlineKeyboardButton(responses['share'][lang(cid)], switch_inline_query="{} {}".format(region, summoner)))
                bot.send_message(
                    cid,
                    res_text,
                    parse_mode="Markdown",
                    reply_markup=keyboard)
            else:
                bot.send_message(
                    cid,
                    res_text,
                    parse_mode="Markdown")
        else:
            bot.send_message(cid, responses['me_error'][lang(cid)])
    else:
        bot.send_message(cid, responses['not_user'])