# -*- coding: utf-8 -*-

from config import *
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
        # if not is_recent(m):
        #     return None
        if is_banned(uid) or is_banned(cid):
            try:
                botan.track(
                    botan_token,
                    cid,
                    to_json(m),
                    "msg from banned: [" + str(cid) + "] [" + str(uid) + "]"
                )
            except:
                pass
            return None
        if m.content_type == 'text':
            if m.text.lower() in easter_eggs:
                try:
                    botan.track(
                        botan_token,
                        cid,
                        to_json(m),
                        "Easteregg: " + m.text.lower()
                    )
                except:
                    pass
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
            log(cid, log_line)
            if extra["log"]:
                try:
                    logBot.send_message(52033876, log_line)
                except:
                    pass
        elif m.content_type in content_types:
            if extra["log"]:
                try:
                    bot.send_message(-32461390, "Chat ID: " + str(m.chat.id) + "\nUser ID: " + str(m.from_user.id) + "\nMensaje ID: " + str(m.message_id) + "\nNombre: " + str(
                        m.from_user.first_name) + "\nAlias: @" + str(m.from_user.username) + "\nTipo de archivo: " + str(m.content_type))
                    bot.forward_message(-32461390, m.chat.id, m.message_id)
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
        champ_key = separe[0]
        if separe[0].lower() == 'wukong':
            separe[0] = 'monkeyking'
        elif separe[0].lower() in ['monkeyking', 'bardo']:
            separe[0] = 'nigro'
        # if separe[0] in backward:
            #separe[0] = backward[separe[0]]
        for x in data[lang(cid)]:
            if separe[0].lower() == data[lang(cid)][x]['key'].lower():
                if is_banned(uid) or is_banned(cid):
                    if not extra['muted']:
                        bot.send_chat_action(cid, 'typing')
                        bot.reply_to(m, responses['banned'])
                    return None
                if len(separe) == 1:
                    try:
                        botan.track(
                            botan_token,
                            cid,
                            to_json(m),
                            "CHAMP: " + no_namebot[0].lower()
                        )
                    except:
                        pass
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
                                    botan.track(
                                        botan_token,
                                        cid,
                                        to_json(m),
                                        "SKIN: " + no_namebot[0].lower()
                                    )
                                except:
                                    pass
                                try:
                                    bot.send_photo(
                                        cid, file_ids[
                                            no_namebot[0].lower()], caption=num['name'])
                                    #bot.send_message( cid, file_ids[no_namebot[0].lower()] + '\n\n' + num['name'])
                                except:
                                    bot.send_chat_action(cid, 'typing')
                                    bot.send_message(
                                        cid, responses['champ_error'][lang(cid)])
                        # if len(data[lang(cid)][x]['skins']) > int(separe[1]):
                            # Poner bot.send_photo( cid, file_ids[no_namebot[0].lower()], caption=data[lang(cid)][x]['skins'][int(separe[1])]['name'])
                            # try:
                                #bot.send_message( cid, file_ids[no_namebot[0].lower()] + '\n\n' + data[lang(cid)][x]['skins'][int(separe[1])]['name'])
                            # except:
                                #bot.send_message( cid, responses['champ_error'][lang(cid)])
                    elif separe[1].lower() == 'extra':
                        txt += champ_info(data[lang(cid)][x], cid, separe[0])
                    # else:
                        # Mensaje de error ¿?
                        #txt += 'Error, prueba con /' + data[lang(cid)][x]['name'] + ' para ver info básica del campeón, /' + data[lang(cid)][x]['name'] + '_X para ver la skin número X de ' + data[lang(cid)][x]['name'] + ' o /' + data[lang(cid)][x]['name'] + '_extra para ver información detallada.'
                    break
        if txt:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(cid, txt, parse_mode="Markdown")
    # else:
        #bot.send_message( cid, responses['not_user'])


def champ_basic(chmp, cid):
    if chmp['key'] in backward:
        key = backward[chmp['key']]
        key2 = chmp['key']
    else:
        key = chmp['key']
        key2 = chmp['key']
    txt = '_' + chmp['name'] + ', ' + chmp['title'] + '_'
    # Roles
    txt += '\n⁣  *' + responses['champ_info']['tags'][lang(cid)] + '*: '
    i = 0
    for tag in chmp['tags']:
        txt += '_' + responses['tags'][tag][lang(cid)] + '_'
        if i == 0:
            txt += ', '
        i += 1
    txt += '\n\n[BUILD](http://www.probuilds.net/champions/details/' + key2 + ')'
    # Descripción
    if lang(cid) != 'fa':
        txt += '\n\n_' + chmp['blurb'].replace('<br><br>', '\n') + '_ ' + '[' + responses['continue'][lang(
            cid)] + '](http://gameinfo.euw.leagueoflegends.com/' + lang(cid) + '/game-info/champions/' + key.lower() + '/)'
    else:
        txt += '\n\n_' + chmp['blurb'].replace('<br><br>', '\n') + '_ ' + '[' + responses['continue'][lang(
            cid)] + '](http://gameinfo.euw.leagueoflegends.com/en/game-info/champions/' + key.lower() + '/)'
    # Skins
    txt += '\n\n*Skins:*'
    for skin in chmp['skins']:
        if skin['num'] != 0:
            txt += '\n⁣  /' + key + '\_' + \
                str(skin['num']) + ': ' + skin['name']
    # txt += '\n\n' + responses['guide'][lang(cid)] #%(champ_key.lower())
    txt += '\n\n' + responses['extra_info'][lang(cid)] + ' /' + key + '\_extra'
    return txt


def champ_info(chmp, cid, key):
    # Nombre + título
    txt = '*' + chmp['name'] + ', ' + chmp['title'] + '*'
    # Roles
    #txt += '\n⁣  *' + responses['champ_info']['tags'][lang(cid)] + '*: '
    #i = 0
    # for tag in chmp['tags']:
    #txt += '_' + responses['tags'][tag][lang(cid)] + '_'
    # if i == 0:
    #txt += ', '
    #i +=1
    # Descripción
    #txt += '\n\n_' + chmp['blurb'] + '_ ' + '[' + responses['continue'][lang(cid)] + '](http://gameinfo.euw.leagueoflegends.com/' + lang(cid) + '/game-info/champions/' + key.lower() + '/)'
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
    txt += '\n*_' + chmp['passive']['description'].replace(
        '<br>', '\n').replace(
        '<mainText>', '').replace(
            '</mainText>', '') + '_\n'
    # Hechizos
    i = 0
    j = ['Q', 'W', 'E', 'R']
    for habilidad in chmp['spells']:
        if i in range(4):
            txt += '\n*' + j[i] + ': ' + habilidad['name'] + '*'
            txt += '\n *CD:* _' + habilidad['cooldownBurn'] + '_'
            txt += '\n_' + \
                remove_tag(habilidad['description'].replace('<br>', '\n')) + '_' + '\n'
            i += 1
        else:
            break
    return txt
