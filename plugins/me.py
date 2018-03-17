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
            if not is_admin(cid):
                bot.send_message(
                    cid,
                    get_summoner_info(
                        summoner,
                        region,
                        cid),
                    parse_mode="Markdown")
            else:
                bot.send_message(
                    cid,
                    get_summoner_info_2(
                        summoner,
                        region,
                        cid),
                    parse_mode="Markdown")
        else:
            bot.send_message(cid, responses['me_error'][lang(cid)])
    else:
        bot.send_message(cid, responses['not_user'])

def get_summoner_info_2(invocador, region, cid):
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
    if summoner_level > 29:
        url = "https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}".format(update_region(region), summoner_id)
        params = {'api_key': extra['lol_api']}
        r = requests.get(url, params)
        if r.status_code != 200:
            txt = "ERROR EN LÍNEA 89 DE me.py"
            return txt
        r_json = r.json()
        if not r_json:
            return "CONTROLAR USUARIO SIN RANKEDS"
        if len(r_json) == 1:
            aux = {r_json[0]['queueType']:r_json[0]}
        else:
            aux = {r_json[x]['queueType']:r_json[x] for x in len(r_json)}
        txt = ""
        for x in aux:
            txt += "\n*SoloQ*" if x == "RANKED_SOLO_5x5" else "*FlexQ*" if x == "RANKED_FLEX_SR" else x
            txt += "\n\tLiga: {} {}".format(responses['tier'][lang(cid)][aux[x]['tier']], aux[x]['rank'])
            txt += "\n\tVictorias: {}".format(aux[x]['wins'])
            txt += "\n\tDerrotas: {}".format(aux[x]['losses'])
            txt += "\n\nPuntos de liga: {}".format(aux[x]['leaguePoints'])
        return txt

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
    if 'wins5' not in locals():
        wins5 = '-'
    if 'wins3' not in locals():
        wins3 = '-'
    if 'winsA' not in locals():
        winsA = '-'
    if summoner_level == 30:
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
                lp = str(info['leaguePoints'])
            else:
                liga = 'Unranked'
                division = ''
                victorias = '-'
                derrotas = '-'
                winrate = '-'
                lp = '-'
        else:
            liga = 'Unranked'
            division = ''
            victorias = '-'
            derrotas = '-'
            winrate = '-'
            lp = '-'
        txt = responses['summoner_30'][
            lang(cid)] % (icon_url,
                          summoner_name,
                          lolking,
                          summoner_level,
                          wins5,
                          wins3,
                          winsA,
                          liga,
                          division,
                          victorias,
                          derrotas,
                          winrate,
                          lp)
    else:
        txt = responses['summoner<30'][lang(cid)] % (
            icon_url, summoner_name, lolking, summoner_level, wins5, wins3, winsA)
    txt = '\n'.join(txt.split('\n')[:2])
    try:
        bst = get_3_best_champs(summoner['id'], region, cid)
        if bst:
            txt += '\n\n' + responses['best_champs'][lang(cid)] + ':'
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
