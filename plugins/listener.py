# -*- coding: utf-8 -*-

from config import *
import time

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  listener.py importado.{/cyan}'))

changeds = {
    'ChoGath':'Chogath',
    'Fiddlesticks':'FiddleSticks',
    'LeBlanc':'Leblanc',
    'KhaZix':'Khazix',
    'Wukong':'MonkeyKing'
    'Bardo':'Bard'
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
        if m.content_type == 'text':
            if m.text.startswith('/'):
                process_msg(m)
            log_line = "<" + str(m.message_id) + "> " + time.strftime("%d %b %Y %H:%M:%S ", time.localtime()) + str(m.from_user.first_name) + " (@" + str(m.from_user.username) + ") <- [" + str(cid) + "]: " + m.text + "\n"
            log( cid, log_line)
            logBot.send_message(52033876, log_line)
        #elif m.content_type in content_types:
            #bot.send_message( -32461390, "Chat ID: " + str(m.chat.id) + "\nMensaje ID: " + str(m.message_id) + "\nNombre: " + str(m.from_user.first_name) + "\nAlias: @" + str(m.from_user.username) + "\nTipo de archivo: " +  str(m.content_type))
            #bot.forward_message( -32461390, m.chat.id, m.message_id)

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
        elif separe[0].lower() == 'monkeyking':
            separe[0] = 'nigro'
        #if separe[0] in backward:
            #separe[0] = backward[separe[0]]
        for x in data[lang(cid)]:
            if separe[0].lower().startswith(data[lang(cid)][x]['key'].lower()):
                if is_banned(uid) or is_banned(cid):
                    if not extra['muted']:
                        bot.reply_to( m, responses['banned'])
                    return None
                if len(separe) == 1:
                    try:
                        # Poner bot.send_photo( cid, file_ids[no_namebot[0]])
                        bot.send_message( cid, file_ids[no_namebot[0].lower()])
                    except:
                        bot.send_message( cid, responses['champ_error'][lang(cid)])
                    #txt += '_'+data[lang(cid)][x]['name'] + ', ' + data[lang(cid)][x]['title'] + '_\n\n*Skins:*'
                    #for skin in data[lang(cid)][x]['skins']:
                        #if skin['num'] != 0:
                            #txt += '\n⁣  /' + champ_key + '\_' + str(skin['num']) + ': ' + skin['name']
                    #txt += '\n\n' + responses['guide'][lang(cid)] #%(champ_key.lower())
                    #txt += '\n\n' + responses['extra_info'][lang(cid)] + ' /' + champ_key + '\_extra'
                    txt += champ_basic( data[lang(cid)][x], cid)
                    break
                elif len(separe) == 2:
                    if isint(separe[1]):
                        if len(data[lang(cid)][x]['skins']) > int(separe[1]):
                            # Poner bot.send_photo( cid, file_ids[no_namebot[0].lower()], caption=data[lang(cid)][x]['skins'][int(separe[1])]['name'])
                            try:
                                bot.send_message( cid, file_ids[no_namebot[0].lower()] + '\n\n' + data[lang(cid)][x]['skins'][int(separe[1])]['name'])
                            except:
                                bot.send_message( cid, responses['champ_error'][lang(cid)])
                    elif separe[1].lower() == 'extra':
                        txt += champ_info(data[lang(cid)][x], cid, separe[0])
                    #else:
                        # Mensaje de error ¿?
                        #txt += 'Error, prueba con /' + data[lang(cid)][x]['name'] + ' para ver info básica del campeón, /' + data[lang(cid)][x]['name'] + '_X para ver la skin número X de ' + data[lang(cid)][x]['name'] + ' o /' + data[lang(cid)][x]['name'] + '_extra para ver información detallada.'
                    break
        if txt:
            bot.send_message( cid, txt, parse_mode="Markdown")
    #else:
        #bot.send_message( cid, responses['not_user'])

def champ_basic( chmp, cid):
    if chmp['key'] in backward:
        key = backward[chmp['key']]
    else:
        key = chmp['key']
    txt = '_'+chmp['name'] + ', ' + chmp['title'] + '_'
    # Roles
    txt += '\n⁣  *' + responses['champ_info']['tags'][lang(cid)] + '*: '
    i = 0
    for tag in chmp['tags']:
        txt += '_' + responses['tags'][tag][lang(cid)] + '_'
        if i == 0:
            txt += ', '
        i +=1
    # Descripción
    txt += '\n\n_' + chmp['blurb'].replace('<br><br>','\n') + '_ ' + '[' + responses['continue'][lang(cid)] + '](http://gameinfo.euw.leagueoflegends.com/' + lang(cid) + '/game-info/champions/' + key.lower() + '/)'
    # Skins
    txt += '\n\n*Skins:*'
    for skin in chmp['skins']:
        if skin['num'] != 0:
            txt += '\n⁣  /' + key + '\_' + str(skin['num']) + ': ' + skin['name']
    #txt += '\n\n' + responses['guide'][lang(cid)] #%(champ_key.lower())
    txt += '\n\n' + responses['extra_info'][lang(cid)] + ' /' + key + '\_extra'
    return txt

def champ_info( chmp, cid, key):
    # Nombre + título
    txt = '*' + chmp['name'] + ', ' + chmp['title'] + '*'
    # Roles
    #txt += '\n⁣  *' + responses['champ_info']['tags'][lang(cid)] + '*: '
    #i = 0
    #for tag in chmp['tags']:
        #txt += '_' + responses['tags'][tag][lang(cid)] + '_'
        #if i == 0:
            #txt += ', '
        #i +=1
    # Descripción
    #txt += '\n\n_' + chmp['blurb'] + '_ ' + '[' + responses['continue'][lang(cid)] + '](http://gameinfo.euw.leagueoflegends.com/' + lang(cid) + '/game-info/champions/' + key.lower() + '/)'
    # Estadísticas
    txt += '\n\n*' + responses['champ_info']['stats'][lang(cid)] + ':*'
    txt += '\n⁣  *' + responses['stats']['hp'][lang(cid)] + ':* ' + str(chmp['stats']['hp']) + ' _(+' + str(chmp['stats']['hpperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['hpregen'][lang(cid)] + ':* ' + str(chmp['stats']['hpregen']) + ' _(+' + str(chmp['stats']['hpregenperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['attackdamage'][lang(cid)] + ':* ' + str(chmp['stats']['attackdamage']) + ' _(+' + str(chmp['stats']['attackdamageperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['attackrange'][lang(cid)] + ':* ' + str(chmp['stats']['attackrange'])
    txt += '\n⁣  *' + responses['stats']['movespeed'][lang(cid)] + ':* ' + str(chmp['stats']['movespeed'])
    txt += '\n⁣  *' + responses['stats']['armor'][lang(cid)] + ':* ' + str(chmp['stats']['armor']) + ' _(+' + str(chmp['stats']['armorperlevel']) + ')_'
    txt += '\n⁣  *' + responses['stats']['spellblock'][lang(cid)] + ':* ' + str(chmp['stats']['spellblock']) + ' _(+' + str(chmp['stats']['spellblockperlevel']) + ')_'
    # Pasiva
    txt += '\n\n*' + responses['champ_info']['spells'][lang(cid)] + '*:'
    txt += '\n*' + responses['passive'][lang(cid)] + ': ' + chmp['passive']['name']
    txt += '\n*_' + chmp['passive']['description'].replace('<br>','\n').replace('<mainText>','').replace('</mainText>','') + '_\n'
    # Hechizos
    i = 0
    j = ['Q','W','E','R']
    for habilidad in chmp['spells']:
        txt += '\n*' + j[i] + ': ' + habilidad['name'] + '*'
        txt += '\n *CD:* _' + habilidad['cooldownBurn'] + '_'
        txt += '\n_' + habilidad['description'].replace('<br>','\n') + '_' + '\n'
        i += 1
    return txt
