# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  .py importado.{/cyan}'))


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
        if not is_beta(uid):
            return
        if users[str(uid)]['summoner'] and users[str(uid)]['server']:
            bot.send_message(
                cid, get_summoner_info(
                    users[
                        str(uid)]['summoner'], users[
                        str(uid)]['server'], cid), parse_mode="Markdown")
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
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    summoner_level = summoner['summonerLevel']
    partidas = lol_api.get_stat_summary(
        summoner_id, region=region, season=None)
    if 'playerStatSummaries' in partidas:
        for data in partidas['playerStatSummaries']:
            if data['playerStatSummaryType'] == player_stat_summary_types[0]:
                normales = data
                wins5 = str(normales['wins'])
            elif data['playerStatSummaryType'] == player_stat_summary_types[1]:
                tresVtres = data
                wins3 = str(tresVtres['wins'])
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
            lang(cid)] % (summoner_name,
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
            summoner_name, summoner_level, wins5, wins3, winsA)
    return txt
