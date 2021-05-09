# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  match.py importado.{/cyan}'))

locales = {
    "es": "es_ES",
    "en": "en_US",
    "it": "it_IT",
    "de": "de_DE",
    "pt": "pt_BR",
    "pl": "pl_PL",
    "ru": "ru_RU",
    "th": "th_TH",
    "el": "el_GR",
    "fr": "fr_FR",
    "fa": "en_US",
    "tr": "tr_TR",
    "ro": "ro_RO",
    "ar": "en_US"
}

platform = {
    "euw": "EUW1",
    "eune": "EUN1",
    "br": "BR1",
    "na": "NA1",
    "las": "LA2",
    "lan": "LA1",
    "kr": "KR",
    "tr": "TR1",
    "ru": "RU",
    "oce": "OC1"
}


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'MECZ',
        'PARTIDA',
        'МАТЧ',
        'MATCH',
        'PARTITA',
        'SPIEL',
        'PARTIE',
        'KARŞILAŞMA',
        'MECI'])
@bot.message_handler(commands=['match'])
def command_match(m):
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
        txt = responses['match_1'][lang(cid)]
        for region in ['euw', 'eune', 'br', 'na',
                       'las', 'lan', 'kr', 'tr', 'ru', 'oce']:
            txt += '\n/match\_' + region + \
                responses['match_3'][lang(cid)] + '*' + region.upper() + '*'
        txt += '\n' + responses['match_2'][lang(cid)]
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, txt, parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text.split(' ')[0].split('@')[0] in [
        '/match_euw',
        '/match_eune',
        '/match_br',
        '/match_na',
        '/match_las',
        '/match_lan',
        '/match_kr',
        '/match_tr',
        '/match_ru',
        '/match_oce'])
def match_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        invocador = ' '.join(m.text.split(' ')[1:])
        cmd = m.text.lstrip('/').split(' ')[0].split('@')[0]
        region = cmd.split('_')[1]
        if not invocador:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['no_summoner'][
                    lang(cid)] %
                (cmd), parse_mode="Markdown")
        else:
            get_match_info(invocador, region, cid)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])


@bot.inline_handler(
    lambda query: len(
        query.query.split()) > 1 and query.query.split()[0] in [
            '#euw',
            '#eune',
            '#br',
            '#na',
            '#las',
            '#lan',
            '#kr',
            '#tr',
            '#ru',
        '#oce'])
def query_summoner(q):
    cid = q.from_user.id
    if is_banned(cid):
        return None
    invocador = q.query.split(None, 1)[1]
    region = q.query.split()[0].strip('#')
    to_send = list()
    try:
        summoner = get_summoner(name=invocador, region=update_region(region))
    except:
        pass
    else:
        if get_match_info(
                invocador,
                region,
                cid,
                inline=True) != 'match_error':
            aux = types.InlineQueryResultArticle(
                "1",
                '[' + region.upper() + '] ' + summoner['name'],
                types.InputTextMessageContent(
                    get_match_info(
                        invocador,
                        region,
                        cid,
                        inline=True),
                    parse_mode="Markdown",
                    disable_web_page_preview=True),
                description=responses['inline_match_d'][
                    lang(cid)].format(
                    summoner['name']),
                thumb_url='http://i.imgur.com/IRTLKz4.jpg')
            to_send.append(aux)
        else:
            aux = types.InlineQueryResultArticle(
                "1",
                responses['inline_match_error'][
                    lang(cid)],
                types.InputTextMessageContent(
                    responses['match_error'][
                        lang(cid)] %
                    (summoner['name']),
                    parse_mode="Markdown"),
                description=responses['match_error'][
                    lang(cid)] %
                (summoner['name']),
                thumb_url='http://i.imgur.com/IRTLKz4.jpg')
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


def get_match_info(invocador, region, cid, inline=False):
    azul = {}
    rojo = {}
    txt = ""
    try:
        summoner = get_summoner(name=invocador, region=update_region(region))
    except:
        if not inline:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['summoner_error'][
                    lang(cid)] %
                (invocador, region.upper()), parse_mode="Markdown")
        return None
    campeones = data['keys']
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    try:
        partida = get_current_game(
            summoner_id=summoner_id,
            region=update_region(region))
    except:
        if not inline:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid,
                responses['match_error'][
                    lang(cid)] %
                (summoner_name),
                parse_mode="Markdown")
        return 'match_error'
    for jugadores in partida['participants']:
        if jugadores['teamId'] == 100:
            try:
                azul[str(jugadores['summonerName'])] = str(
                    campeones[str(jugadores['championId'])]['name'])
            except:
                azul[str(jugadores['summonerName'])] = 'Taliyah'
        else:
            try:
                rojo[str(jugadores['summonerName'])] = str(
                    campeones[str(jugadores['championId'])]['name'])
            except:
                rojo[str(jugadores['summonerName'])] = 'Taliyah'
    txt += responses['match_blue'][lang(cid)] % (partida['gameMode'])
    for a, b in azul.items():
        txt += '\n\n' + get_summoner_info_match(
            invocador=a,
            region=region,
            champion=b,
            cid=cid
        )
    txt += '\n\n' + responses['match_red'][lang(cid)]
    for a, b in rojo.items():
        txt += '\n\n' + get_summoner_info_match(
            invocador=a,
            region=region,
            champion=b,
            cid=cid
        )
    if inline:
        return txt
    else:
        bot.send_message(cid, txt, parse_mode="Markdown",
                         disable_web_page_preview=True)


def get_summoner_info_match(invocador, region, champion, cid):
    try:
        summoner = get_summoner(name=invocador, region=update_region(region))
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    lolking = "http://www.lolking.net/summoner/" + \
        region + "/" + str(summoner_id)
    summoner_level = summoner['summonerLevel']
    txt = responses['summoner<30_2'][lang(cid)].format(summoner_name, lolking, summoner_level, champion)
    return txt
