# -*- coding: utf-8 -*-

from config import *
import requests

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  summoner.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'PRZYWOŁYWACZ',
        'INVOCADOR',
        'SUMMONER',
        'INVOCATOR',
        'EVOCATORE',
        'ПРИЗЫВАТЕЛЬ',
        'BESCHWÖRER',
        'INVOCATEUR',
        'SİHİRDAR'])
@bot.message_handler(commands=['summoner'])
def command_summoner(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['summoner_1'][lang(cid)]
        for region in ['euw', 'eune', 'br', 'na',
                       'las', 'lan', 'kr', 'tr', 'ru', 'oce']:
            txt += '\n/' + region + \
                responses['summoner_3'][lang(cid)] + '*' + region.upper() + '*'
        txt += '\n' + responses['summoner_2'][lang(cid)]
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, txt, parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text.split(' ')[0].split('@')[0].lower() in [
        '/euw',
        '/eune',
        '/br',
        '/na',
        '/las',
        '/lan',
        '/kr',
        '/tr',
        '/ru',
        '/oce'])
def summoner_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        summoner = ' '.join(m.text.split(' ')[1:])
        region = m.text.lstrip('/').split(' ')[0].split('@')[0].lower()
        
        if not summoner:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['no_summoner'][
                    lang(cid)] %
                (region), parse_mode="Markdown")
        else:
            res_text, res_info = get_summoner_info(
                    summoner,
                    region,
                    cid)
            if res_info:
                keyboard = types.InlineKeyboardMarkup()
                c_data = {
                    "r":region,
                    "s":summoner,
                    "a":"h"
                }
                keyboard.add(types.InlineKeyboardButton(responses['matches_history'][lang(cid)], callback_data=json.dumps(c_data)))
                keyboard.add(types.InlineKeyboardButton(responses['share'][lang(cid)], switch_inline_query="{} {}".format(region, summoner)))
                bot.send_chat_action(cid, 'typing')
                bot.send_message(
                    cid,
                    res_text,
                    parse_mode="Markdown",
                    reply_markup=keyboard)
            else:
                bot.send_message(cid, res_text)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.inline_handler(
    lambda query: len(
        query.query.split()) > 1 and query.query.split()[0] in [
            'euw',
            'eune',
            'br',
            'na',
            'las',
            'lan',
            'kr',
            'tr',
            'ru',
            'oce'])
def query_summoner(q):
    cid = q.from_user.id
    if is_banned(cid):
        return None
    invocador = q.query.split(None, 1)[1]
    region = q.query.split()[0]
    to_send = list()
    try:
        summoner = get_summoner(name=invocador, region=update_region(region))
    except:
        pass
    else:
        lattest_version = get_static_version()
        icon_id = summoner['profileIconId']
        icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
            lattest_version, icon_id)
        res_text, res_info = get_summoner_info(
                invocador,
                region,
                cid)
        if res_info:
            keyboard = types.InlineKeyboardMarkup()
            c_data = {
                    "r":region,
                    "s":invocador,
                    "a":"h"
                }
            # keyboard.add(types.InlineKeyboardButton(responses['matches_history'][lang(cid)], callback_data=json.dumps(c_data)))
            keyboard.add(types.InlineKeyboardButton(responses['share'][lang(cid)], switch_inline_query="{} {}".format(region, invocador)))

            get_summoner_info(
                        invocador,
                        region,
                        cid)[0]
            aux = types.InlineQueryResultArticle(
                "1",
                '[' + region.upper() + '] ' + summoner['name'],
                types.InputTextMessageContent(
                    res_text,
                    parse_mode="Markdown"),
                thumb_url=icon_url,
                reply_markup=keyboard,
                description=responses['inline_summoner_d'][
                    lang(cid)].format(
                    summoner['name']))
            to_send.append(aux)
    if to_send:
        bot.answer_inline_query(q.id, to_send, cache_time=1)
    else:
        aux = types.InlineQueryResultArticle(
            "1",
            responses['inline_me_error_ttl_2'][
                lang(cid)],
            types.InputTextMessageContent(
                responses['summoner_error'][
                    lang(cid)] %
                (invocador,
                 region.upper()),
                parse_mode="Markdown"),
            description=responses['inline_me_error_d_2'][
                lang(cid)] %
            (invocador,
             region.upper()),
            thumb_url='http://i.imgur.com/IRTLKz4.jpg')
        bot.answer_inline_query(q.id, [aux], cache_time=1)