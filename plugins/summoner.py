# -*- coding: utf-8 -*-

from config import *
import requests

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  summoner.py importado.{/cyan}'))


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
    try:
        send_udp('summoner')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
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
    try:
        send_udp(m.text.lstrip('/').split(' ')[0].split('@')[0].lower())
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
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
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid,
                get_summoner_info(
                    summoner,
                    region,
                    cid),
                parse_mode="Markdown")
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
        summoner = lol_api.get_summoner(name=invocador, region=update_region(region))
    except:
        pass
    else:
        lattest_version = static_versions()
        icon_id = summoner['profileIconId']
        icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
            lattest_version, icon_id)
        aux = types.InlineQueryResultArticle(
            "1",
            '[' + region.upper() + '] ' + summoner['name'],
            types.InputTextMessageContent(
                get_summoner_info(
                    invocador,
                    region,
                    cid),
                parse_mode="Markdown"),
            thumb_url=icon_url,
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

def get_summoner_info(invocador, region, cid):
    try:
        summoner = lol_api.get_summoner(name=invocador, region=update_region(region))
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    lattest_version = static_versions()
    icon_id = summoner['profileIconId']
    icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
        lattest_version, icon_id)
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    lolking = "http://www.lolking.net/summoner/" + \
        region + "/" + str(summoner_id)
    summoner_level = summoner['summonerLevel']
    txt = responses['summoner_30_beta_1'][lang(cid)].format(icon_url, summoner_name, lolking, summoner_level)
    if summoner_level > 29:
        url = "https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}".format(update_region(region), summoner_id)
        params = {'api_key': extra['lol_api']}
        r = requests.get(url, params)
        if r.status_code != 200:
            txt = "ERROR EN LÍNEA 89 DE me.py"
            return txt
        r_json = r.json()
        if not r_json:
            aux = {}
        if len(r_json) == 1:
            aux = {r_json[0]['queueType']:r_json[0]}
        else:
            aux = {x['queueType']:x for x in r_json}
        for x in aux:
            txt += responses['summoner_30_beta_2'][lang(cid)].format(
                        "SoloQ" if x == "RANKED_SOLO_5x5" else "FlexQ" if x == "RANKED_FLEX_SR" else x,
                        responses['tier'][lang(cid)][aux[x]['tier']],
                        aux[x]['rank'],
                        aux[x]['wins'],
                        aux[x]['losses'],
                        aux[x]['leaguePoints'])
        try:
            bst = get_3_best_champs(summoner['id'], region, cid)
            if bst:
                txt += '\n\n*' + responses['best_champs'][lang(cid)] + '*:'
                for x, y in bst.items():
                    txt += '\n- ' + x + ' _(Level: ' + y + ')_'
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    return txt

def get_3_best_champs(summonerId, region, cid):
    url = 'https://{}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}'.format(
        update_region(region.lower()), summonerId)
    params = {
        "api_key": extra['lol_api']
    }
    jstr = requests.get(
        url=url,
        params=params
    )
    if jstr.status_code != 200:
        return None
    else:
        return OrderedDict([(data[lang(cid)][data['keys'][str(x['championId'])]['key']][
                           'name'], str(x['championLevel'])) for x in jstr.json()[:3]])
