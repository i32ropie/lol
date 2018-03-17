# -*- coding: utf-8 -*-

from config import *
import requests


print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  me.py importado.{/cyan}'))


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


@bot.message_handler(commands=['me'])
def command_m(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('me')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        try:
            summoner = db.usuarios.find_one(str(uid))['summoner']
            region = db.usuarios.find_one(str(uid))['server']
        except:
            bot.send_message(cid, responses['me_error'][lang(cid)])
            return
        if summoner and region:
            bot.send_message(
                cid,
                get_summoner_info(
                    summoner,
                    region,
                    cid),
                parse_mode="Markdown")
        else:
            bot.send_message(cid, responses['me_error'][lang(cid)])
    else:
        bot.send_message(cid, responses['not_user'])

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
