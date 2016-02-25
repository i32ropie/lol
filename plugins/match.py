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
    "fr": "fr_FR",
    "fa": "en_US"
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


@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in [
                     'MECZ', 'PARTIDA', 'МАТЧ', 'MATCH', 'PARTITA', 'SPIEL', 'PARTIE'])
@bot.message_handler(commands=['match'])
def command_match(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/match"
        )
    except:
        pass
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
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            m.text.split(' ')[0].split('@')[0]
        )
    except:
        pass
    if is_banned(uid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        if cid < 0:
            bot.send_message(cid, responses['private'][lang(cid)])
            return None
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


def get_match_info(invocador, region, cid):
    azul = {}
    rojo = {}
    try:
        summoner = lol_api.get_summoner(name=invocador, region=region)
    except:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid, responses['summoner_error'][
                lang(cid)] %
            (invocador, region.upper()), parse_mode="Markdown")
        return None
    campeones = lol_api.static_get_champion_list(
        region=region,
        locale=locales[
            lang(cid)],
        champ_data='altimages',
        data_by_id=True)['data']
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    try:
        partida = lol_api.get_current_game(
            summoner_id=summoner_id,
            platform_id=platform[region],
            region=region)
    except:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            responses['match_error'][
                lang(cid)] %
            (summoner_name),
            parse_mode="Markdown")
        return None
    for jugadores in partida['participants']:
        if jugadores['teamId'] == 100:
            azul[str(jugadores['summonerName'])] = str(
                campeones[str(jugadores['championId'])]['name'])
        else:
            rojo[str(jugadores['summonerName'])] = str(
                campeones[str(jugadores['championId'])]['name'])
    bot.send_chat_action(cid, 'typing')
    bot.send_message(
        cid, responses['match_blue'][
            lang(cid)] %
        (partida['gameMode']))
    for a, b in azul.items():
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            get_summoner_info_2(
                invocador=a,
                region=region,
                champion=b,
                cid=cid),
            parse_mode="Markdown")
    bot.send_chat_action(cid, 'typing')
    bot.send_message(cid, responses['match_red'][lang(cid)])
    for a, b in rojo.items():
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            get_summoner_info_2(
                invocador=a,
                region=region,
                champion=b,
                cid=cid),
            parse_mode="Markdown")


def get_summoner_info_2(invocador, region, champion, cid):
    try:
        summoner = lol_api.get_summoner(name=invocador, region=region)
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    summoner_level = summoner['summonerLevel']
    if summoner_level == 30:
        try:
            rankeds = lol_api.get_league(
                summoner_ids=[summoner_id], region=region)
        except:
            pass
        if 'rankeds' in locals():
            if rankeds[str(summoner_id)][0]['queue'] == "RANKED_SOLO_5x5":
                for x in rankeds[str(summoner_id)][0]['entries']:
                    if str(x['playerOrTeamId']) == str(summoner_id):
                        info = x
                        break
                division = info['division']
                liga = responses['tier'][
                    lang(cid)][
                    rankeds[
                        str(summoner_id)][0]['tier']]
                victorias = str(info['wins'])
                derrotas = str(info['losses'])
                v1 = float(victorias)
                d1 = float(derrotas)
                w1 = int((v1 / (v1 + d1)) * 100)
                winrate = str(w1).replace('.', '\'') + "%"
            else:
                liga = 'Unranked'
                division = ''
                winrate = '-'
        else:
            liga = 'Unranked'
            division = ''
            winrate = '-'
        txt = responses['summoner_30_2'][lang(cid)] % (
            summoner_name, liga, division, winrate, champion)
    else:
        txt = responses['summoner<30_2'][lang(cid)] % (
            summoner_name, summoner_level, champion)
    return txt
