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


def listener(messages):
    for m in messages:
        cid = m.chat.id
        uid = m.from_user.id
        if is_banned(uid) or is_banned(cid):
            return None
        try:
            send_udp('rcvd')
        except Exception as e:
            bot.send_message(
                52033876,
                send_exception(e),
                parse_mode="Markdown")
        if m.content_type == 'text':
            if m.text.lower() in ['sorcio', 'sorcio84']:
                bot.send_sticker(cid, choice(sorcio))
            if m.text.startswith(
                    '/') and is_user(cid) and m.text not in ['/start', '/stop']:
                process_msg(m)
                try:
                    send_udp('command')
                except Exception as e:
                    bot.send_message(
                        52033876, send_exception(e), parse_mode="Markdown")
            if cid > 0:
                log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                    m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(cid) + "]: " + m.text + "\n"
            else:
                log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(
                    m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(uid) + "][" + str(cid) + "]: " + m.text + "\n"
            if cid in filtered:
                bot.send_message(52033876, log_line)
            elif extra["log"]:
                try:
                    logBot.send_message(52033876, log_line)
                except:
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
                        bot.send_message(
                            52033876, send_exception(e), parse_mode="Markdown")
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
                                    bot.send_message(
                                        52033876, send_exception(e), parse_mode="Markdown")
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
                    elif separe[1].lower() == 'lore':
                        txt += champ_lore(data[lang(cid)][x], cid)
                    break
        if txt:
            if len(separe) == 1:
                keyboard = types.InlineKeyboardMarkup()
                keyboard.add(types.InlineKeyboardButton(responses['share'][lang(cid)], switch_inline_query="c {}".format(separe[0])))
                keyboard.add(types.InlineKeyboardButton(responses['share_skins'][lang(cid)], switch_inline_query="s {}".format(separe[0])))
                bot.send_chat_action(cid, 'typing')
                bot.send_message(cid, txt, parse_mode="Markdown", reply_markup=keyboard)
            else:
                bot.send_chat_action(cid, 'typing')
                bot.send_message(cid, txt, parse_mode="Markdown")


@bot.inline_handler(
    lambda query: query.query.startswith('c ') and len(
        query.query.split()) == 2)
def query_champ_basic(q):
    cid = q.from_user.id
    if is_banned(cid):
        return None
    try:
        to_send = list()
        c_name = q.query.split()[1].lower()
        if c_name == 'wukong':
            c_name = 'monkeyking'
        elif c_name == 'monkeyking':
            c_name = 'wukong'
        for x in data[lang(cid)]:
            #if c_name == data[lang(cid)][x]['key'].lower():
            if data[lang(cid)][x]['key'].lower().startswith(c_name):
                champ = data[lang(cid)][x]
                lattest_version = static_versions()
                thumb = 'http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png'.format(
                    lattest_version, champ['key'])
                txt = champ_basic(data[lang(cid)][x], cid, inline=True)
                aux = types.InlineQueryResultArticle(
                    "1", champ['name'], types.InputTextMessageContent(
                        txt, parse_mode="Markdown"), description=responses['inline_champ_d'][
                        lang(cid)].format(
                        champ['name']), thumb_url=thumb)
                to_send.append(aux)
        if to_send:
            bot.answer_inline_query(q.id, to_send, cache_time=1)
    except:
        pass


@bot.inline_handler(
    lambda query: query.query.startswith('#c ') and len(
        query.query.split()) == 2)
def query_champ_extra(q):
    cid = q.from_user.id
    try:
        to_send = list()
        c_name = q.query.split()[1].lower()
        if c_name == 'wukong':
            c_name = 'monkeyking'
        elif c_name == 'monkeyking':
            c_name = 'wukong'
        for x in data[lang(cid)]:
            #if c_name == data[lang(cid)][x]['key'].lower():
            if data[lang(cid)][x]['key'].lower().startswith(c_name):
                champ = data[lang(cid)][x]
                lattest_version = static_versions()
                thumb = 'http://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png'.format(
                    lattest_version, champ['key'])
                txt = champ_info(data[lang(cid)][x], cid)
                aux = types.InlineQueryResultArticle(
                    "1", champ['name'], types.InputTextMessageContent(
                        txt, parse_mode="Markdown"), description=responses['inline_champ_d'][
                        lang(cid)].format(
                        champ['name']), thumb_url=thumb)
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
        txt += '[⁣](http://ddragon.leagueoflegends.com/cdn/img/champion/splash/' + \
            chmp['key'] + '_0.jpg)'
    # Roles
    txt += '\n⁣*' + responses['champ_info']['tags'][lang(cid)] + '*: '
    i = 0
    if chmp['name'].lower() != 'shen':
        for tag in chmp['tags']:
            txt += '_' + responses['tags'][tag][lang(cid)] + '_'
            if i == 0:
                txt += ', '
            i += 1
    # Descripción
    txt += '\n\n_' + chmp['blurb'].replace(
        '<br><br>', '\n').replace(
        '<br>', '\n') + '_ '
    if not inline:
        txt += '/' + key + '\_lore'
    # Skins
    txt += '\n\n*Skins:*'
    for skin in chmp['skins']:
        if skin['num'] != 0:
            if not inline:
                txt += '\n⁣  /' + key + '\_' + \
                    str(skin['num']) + ': ' + skin['name']
            else:
                txt += '\n  • ' + skin['name']
    txt += '\n\n[BUILD](http://www.probuilds.net/champions/details/' + key2 + ')'
    if not inline:
        txt += '\n\n' + \
            responses['extra_info'][lang(cid)] + ' /' + key + '\_extra'
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
    tooltip = s['sanitizedTooltip']
    for i,x in enumerate(s['effectBurn']):
        tooltip = tooltip.replace("{{{{ e{} }}}}".format(i), x)
    if s.get('vars'):
        for x in s.get('vars'):
            tooltip = tooltip.replace("{{{{ {} }}}}".format(x['key']), str(x['coeff'][0]))
    tooltip = re.sub("\{\{ f[0-9] \}\}", "[0]", tooltip)
    return tooltip


def champ_lore(chmp, cid):
    return remove_tag(chmp['lore'].replace('<br>', '\n'))