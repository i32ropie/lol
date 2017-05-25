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
        summoner = lol_api.get_summoner(name=invocador, region=region)
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    lattest_version = lol_api.static_get_versions()[0]
    icon_id = summoner['profileIconId']
    icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
        lattest_version, icon_id)
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    lolking = "http://www.lolking.net/summoner/" + \
        region + "/" + str(summoner_id)
    summoner_level = summoner['summonerLevel']
    try:
        partidas = lol_api.get_stat_summary(
            summoner_id, region=region, season=None)
    except:
        txt = "Error with RIOT servers :("
        bot.send_message(
            52033876,
            "Error obteniendo información de <{}> en <{}> | {}".format(
                summoner_name,
                region,
                cid))
        return txt
    if 'playerStatSummaries' in partidas:
        for data in partidas['playerStatSummaries']:
            if data['playerStatSummaryType'] == player_stat_summary_types[0]:
                normals = data
                wins5 = str(normals['wins'])
            elif data['playerStatSummaryType'] == player_stat_summary_types[1]:
                v3 = data
                wins3 = str(v3['wins'])
            elif data['playerStatSummaryType'] == player_stat_summary_types[3]:
                arams = data
                winsA = str(arams['wins'])
    if 'wins5' not in locals():
        wins5 = '-'
    if 'wins3' not in locals():
        wins3 = '-'
    if 'winsA' not in locals():
        winsA = '-'
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
    url = 'https://{}.api.pvp.net/championmastery/location/{}/player/{}/topchampions'.format(
        region.lower(), platform[region], summonerId)
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
                           'name'], str(x['championLevel'])) for x in json.loads(jstr.text)])
