# -*- coding: utf-8 -*-

from config import *
from bs4 import BeautifulSoup
import requests
import time

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  listener.py importado.{/cyan}'))

changeds = {
    'ChoGath': 'Chogath',
    'Fiddlesticks': 'FiddleSticks',
    'LeBlanc': 'Leblanc',
    'KhaZix': 'Khazix',
    'Wukong': 'MonkeyKing',
    'Bardo': 'Bard'
}

backward = {
    'Chogath': 'ChoGath',
    'FiddleSticks': 'Fiddlesticks',
    'Leblanc': 'LeBlanc',
    'Khazix': 'KhaZix',
    'MonkeyKing': 'Wukong'
}

content_types = [
    'audio',
    'voice',
    'document',
    'photo',
    'sticker',
    'video'
]

def listener(messages):
    for m in messages:
        cid = m.chat.id
        uid = m.from_user.id
        if is_banned(uid) or is_banned(cid):
            return None
        try:
            send_udp('rcvd')
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
        if m.content_type == 'text':
            if m.text.startswith('/'):
                try:
                    send_udp('command')
                except Exception as e:
                    bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
            if m.text.lower() in easter_eggs:
                try:
                    send_udp('easteregg')
                except Exception as e:
                    bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
                bot.send_message(
                    cid,
                    easter_eggs[
                        m.text.lower()],
                    reply_to_message_id=m.message_id,
                    parse_mode="Markdown")
            if m.text.startswith('/'):
                process_msg(m)
            if cid > 0:
                log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                    m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(cid) + "]: " + m.text + "\n"
            else:
                log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                    m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(uid) + "][" + str(cid) + "]: " + m.text + "\n"
            if extra["log"]:
                try:
                    logBot.send_message(52033876, log_line)
                except:
                    pass
        elif m.content_type in content_types:
            if extra["log"]:
                try:
                    logBot.send_message(-1001011373048, "Chat ID: " + str(m.chat.id) + "\nUser ID: " + str(m.from_user.id) + "\nMensaje ID: " + str(
                        m.message_id) + "\nNombre: " + str(m.from_user.first_name) + "\nAlias: @" + str(m.from_user.username) + "\nTipo de archivo: " + str(m.content_type))
                    bot.forward_message(-1001011373048,
                                        m.chat.id, m.message_id)
                except Exception as e:
                    pass

bot.set_update_listener(listener)


def process_msg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_user(cid):
        command = m.text.lstrip('/')
        no_namebot = command.split('@')
        txt = ""
        separe = no_namebot[0].split('_')
        champ_key = separe[0]
        if separe[0].lower() == 'wukong':
            separe[0] = 'monkeyking'
        elif separe[0].lower() in ['monkeyking', 'bardo']:
            separe[0] = 'nigro'
        for x in data[lang(cid)]:
            if separe[0].lower() == data[lang(cid)][x]['key'].lower():
                if is_banned(uid) or is_banned(cid):
                    if not extra['muted']:
                        bot.send_chat_action(cid, 'typing')
                        bot.reply_to(m, responses['banned'])
                    return None
                if len(separe) == 1:
                    try:
                        send_udp('get_champ')
                    except Exception as e:
                        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
                    try:
                        bot.send_photo(cid, file_ids[no_namebot[0].lower()])
                    except:
                        bot.send_chat_action(cid, 'typing')
                        bot.send_message(
                            cid, responses['champ_error'][
                                lang(cid)])
                    txt += champ_basic(data[lang(cid)][x], cid)
                    break
                elif len(separe) == 2:
                    if isint(separe[1]):
                        for num in data[lang(cid)][x]['skins']:
                            if num['num'] == int(separe[1]):
                                try:
                                    send_udp('get_skin')
                                except Exception as e:
                                    bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
                                try:
                                    bot.send_photo(
                                        cid, file_ids[
                                            no_namebot[0].lower()], caption=num['name'])
                                except:
                                    bot.send_chat_action(cid, 'typing')
                                    bot.send_message(
                                        cid, responses['champ_error'][lang(cid)])
                    elif separe[1].lower() == 'extra':
                        txt += champ_info(data[lang(cid)][x], cid)
                    break
        if txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, txt, parse_mode="Markdown")


@bot.inline_handler(lambda query: query.query.startswith('c ') and len(query.query.split()) == 2)
def query_champ_basic(q):
    cid = q.from_user.id
    if is_beta(cid):
        if is_banned(cid):
            return None
        try:
            to_send=list()
            c_name=q.query.split()[1].lower()
            if c_name == 'wukong':
                c_name = 'monkeyking'
            elif c_name == 'monkeyking':
                c_name = 'wukong'
            for x in data[lang(cid)]:
                if c_name == data[lang(cid)][x]['key'].lower():
                    champ = data[lang(cid)][x]
                    lattest_version = lol_api.static_get_versions()[0]
                    thumb='http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png'.format(lattest_version, champ['key'])
                    txt = champ_basic(data[lang(cid)][x], cid, inline=True)
                    aux = types.InlineQueryResultArticle("1",
                            champ['name'],
                            types.InputTextMessageContent(txt, parse_mode="Markdown"),
                            description=responses['inline_champ_d'][lang(cid)].format(champ['name']),
                            thumb_url=thumb)
                    to_send.append(aux)
            if to_send:
                bot.answer_inline_query(q.id, to_send, cache_time=1)
        except:
            pass


@bot.inline_handler(lambda query: query.query.startswith('#c ') and len(query.query.split()) == 2)
def query_champ_extra(q):
    cid = q.from_user.id
    if is_beta(cid):
        try:
            to_send=list()
            c_name=q.query.split()[1].lower()
            if c_name == 'wukong':
                c_name = 'monkeyking'
            elif c_name == 'monkeyking':
                c_name = 'wukong'
            for x in data[lang(cid)]:
                if c_name == data[lang(cid)][x]['key'].lower():
                    champ = data[lang(cid)][x]
                    lattest_version = lol_api.static_get_versions()[0]
                    thumb='http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png'.format(lattest_version, champ['key'])
                    txt = champ_info(data[lang(cid)][x], cid)
                    aux = types.InlineQueryResultArticle("1",
                            champ['name'],
                            types.InputTextMessageContent(txt, parse_mode="Markdown"),
                            description=responses['inline_champ_d'][lang(cid)].format(champ['name']),
                            thumb_url=thumb)
                    to_send.append(aux)
            if to_send:
                bot.answer_inline_query(q.id, to_send, cache_time=1)
        except:
            pass

def champ_basic(chmp, cid, inline=False):
    if chmp['key'] in backward:
        key = backward[chmp['key']]
        key2 = chmp['key']
    else:
        key = chmp['key']
        key2 = chmp['key']
    txt = '_' + chmp['name'] + ', ' + chmp['title'] + '_'
    if inline:
        txt += '[⁣](http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+chmp['key']+'_0.jpg)'
    # Roles
    txt += '\n⁣*' + responses['champ_info']['tags'][lang(cid)] + '*: '
    i = 0
    for tag in chmp['tags']:
        txt += '_' + responses['tags'][tag][lang(cid)] + '_'
        if i == 0:
            txt += ', '
        i += 1
    # Descripción
    if lang(cid) != 'fa':
        txt += '\n\n_' + chmp['blurb'].replace('<br><br>', '\n').replace('<br>', '\n') + '_ ' + '[' + responses['continue'][lang(
            cid)] + '](http://gameinfo.euw.leagueoflegends.com/' + lang(cid) + '/game-info/champions/' + key.lower() + '/)'
    else:
        txt += '\n\n_' + chmp['blurb'].replace('<br><br>', '\n').replace('<br>', '\n') + '_ ' + '[' + responses['continue'][lang(
            cid)] + '](http://gameinfo.euw.leagueoflegends.com/en/game-info/champions/' + key.lower() + '/)'
    # Skins
    txt += '\n\n*Skins:*'
    for skin in chmp['skins']:
        if skin['num'] != 0:
            if not inline:
                txt += '\n⁣  /' + key + '\_' + \
                    str(skin['num']) + ': ' + skin['name']
            else:
                txt += '\n  • ' + skin['name']
    if not inline:
        try:
            r = requests.get('http://www.championselect.net/champions/' + key.lower())
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
        if r.status_code == 200:
            try:
                soup = BeautifulSoup(r.text, 'html.parser')
                weak_against = {x.string.replace("'","").replace(" ","") for x in soup.findAll(class_='weak-block')[0].findAll(class_='name')}
                strong_against = {x.string.replace("'","").replace(" ","") for x in soup.findAll(class_='strong-block')[0].findAll(class_='name')}
                txt += '\n\n' + responses['warning'][lang(cid)]
                txt += '\n' + responses['weak_against'][lang(cid)] + ', /'.join(list(weak_against)[:5])
                txt += '\n' + responses['strong_against'][lang(cid)] + ', /'.join(list(strong_against)[:5])
            except Exception as e:
                bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    txt += '\n\n[BUILD](http://www.probuilds.net/champions/details/' + key2 + ')'
    if not inline:
        txt += '\n\n' + responses['extra_info'][lang(cid)] + ' /' + key + '\_extra'
    return txt


def champ_info(chmp, cid):
    # Nombre + título
    txt = '*' + chmp['name'] + ', ' + chmp['title'] + '*'
    # Estadísticas
    txt += '\n\n*' + responses['champ_info']['stats'][lang(cid)] + ':*'
    txt += '\n⁣  *' + responses['stats']['hp'][lang(cid)] + ':* ' + str(
        chmp['stats']['hp']) + ' _(+' + str(chmp['stats']['hpperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['hpregen'][lang(cid)] + ':* ' + str(
        chmp['stats']['hpregen']) + ' _(+' + str(chmp['stats']['hpregenperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['attackdamage'][lang(cid)] + ':* ' + str(
        chmp['stats']['attackdamage']) + ' _(+' + str(chmp['stats']['attackdamageperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['attackrange'][
        lang(cid)] + ':* ' + str(chmp['stats']['attackrange'])
    txt += '\n⁣  *' + \
        responses['stats']['movespeed'][
            lang(cid)] + ':* ' + str(chmp['stats']['movespeed'])
    txt += '\n⁣  *' + responses['stats']['armor'][lang(cid)] + ':* ' + str(
        chmp['stats']['armor']) + ' _(+' + str(chmp['stats']['armorperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['spellblock'][lang(cid)] + ':* ' + str(
        chmp['stats']['spellblock']) + ' _(+' + str(chmp['stats']['spellblockperlevel']) + ')_'
    # Pasiva
    txt += '\n\n*' + responses['champ_info']['spells'][lang(cid)] + '*:'
    txt += '\n*' + \
        responses['passive'][lang(cid)] + ': ' + chmp['passive']['name']
    txt += '\n*_' + remove_tag(chmp['passive']['description'].replace(
        '<br>', '\n').replace(
        '<mainText>', '').replace(
            '</mainText>', '')) + '_\n'
    # Hechizos
    i = 0
    j = ['Q', 'W', 'E', 'R']
    for habilidad in chmp['spells']:
        if i in range(4):
            txt += '\n*' + j[i] + ': ' + habilidad['name'] + '*'
            txt += '\n *CD:* _' + habilidad['cooldownBurn'] + '_'
            if not is_beta(cid):
                txt += '\n_' + \
                    remove_tag(habilidad['description'].replace('<br>', '\n')) + '_' + '\n'
            else:
                txt += '\n_' + format_spell(habilidad) + '_\n'
            i += 1
        else:
            break
    return txt


def format_spell(s):
    effect = s['effectBurn']
    if 'vars' in s:
        var = s['vars']
    else:
        var = None
    tooltip = s['sanitizedTooltip']
    for x in effect:
            try:
                tooltip = tooltip.replace('{{ e%s }}'%(effect.index(x)), x)
            except Exception as e:
                bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if var:
        for x in var:
                try:
                    tooltip = tooltip.replace('{{ %s }}'%(x['key']), str(x['coeff'][0]))
                except Exception as e:
                    bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    return tooltip
