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
        'EVOCATORE',
        'ПРИЗЫВАТЕЛЬ',
        'BESCHWÖRER',
        'INVOCATEUR'])
@bot.message_handler(commands=['summoner'])
def command_summoner(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/summoner"
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
        botan.track(
            botan_token,
            cid,
            to_json(m),
            m.text.split(' ')[0].split('@')[0].lower()
        )
    except:
        pass
    if is_banned(uid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        invocador = ' '.join(m.text.split(' ')[1:])
        region = m.text.lstrip('/').split(' ')[0].split('@')[0].lower()
        if not invocador:
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
                    invocador,
                    region,
                    cid),
                parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
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
    icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(lattest_version, icon_id)
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    summoner_level = summoner['summonerLevel']
    partidas = lol_api.get_stat_summary(
        summoner_id, region=region, season=None)
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
    if not 'wins5' in locals():
        wins5 = '-'
    if not 'wins3' in locals():
        wins3 = '-'
    if not 'winsA' in locals():
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
            icon_url, summoner_name, summoner_level, wins5, wins3, winsA)
    if is_beta(cid):
        try:
            bst = get_3_best_champs(summoner['id'],region,cid)
            if bst:
                txt += '\n\nBest champions:'
                for x in bst:
                    txt += '\n- ' + x
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    return txt

def get_3_best_champs(summonerId, region, cid):
    url = 'https://global.api.pvp.net/championmastery/location/{}/player/{}/topchampions'.format(regio,platform[region],summonerId)
    bot.send_message(cid, '[DEBUG] url = \n\n' + url + '?api_key='+extra['lol_api'])
    params = {
        "api_key":extra['lol_api']
    }
    jstr = requests.get(
        url=url,
        params=params
    )
    bot.send_message(cid, '[DEBUG] jstr.text = \n\n' + jstr.text)
    if jstr.status_code != 200:
        return None
    else:
        return [data[lang(cid)][data['keys'][str(x['championId'])]['key']]['name'] for x in json.loads(jstr.text)]
