# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  inline_skins.py importado.{/cyan}'))


backward = {
    'Chogath': 'ChoGath',
    'FiddleSticks': 'Fiddlesticks',
    'Leblanc': 'LeBlanc',
    'Khazix': 'KhaZix',
    'MonkeyKing': 'Wukong'
}


@bot.inline_handler(lambda query: query.query.startswith('s ') and len(query.query.split()) == 2)
def query_skins(q):
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
                    champ=data[lang(cid)][x]
                    for i in champ['skins']:
                        aux = types.InlineQueryResultPhoto(str(champ['skins'].index(i)),
                            'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_'+str(i['num'])+'.jpg',
                            'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_'+str(i['num'])+'.jpg',
                            caption=i['name'])
                        to_send.append(aux)
            if to_send:
                bot.answer_inline_query(q.id, to_send)
        except:
            pass


@bot.inline_handler(lambda query: query.query.startswith('c ') and len(query.query.split()) == 2)
def query_skins(q):
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
                    champ=data[lang(cid)][x]
                    txt = champ_basic(data[lang(cid)][x], cid)
                    print('\n'+txt+'\n')
                    aux = types.InlineQueryResultArticle("1",
                            champ['name'],
                            types.InputTextMessageContent(txt,
                                parse_mode="Markdown"),
                            description=responses['inline_champ_d'][lang(cid)],
                            thumb_url='http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_0.jpg')
                    to_send.append(aux)
            if to_send:
                bot.answer_inline_query(q.id, to_send)
        except:
            pass


# @bot.inline_handler(lambda query: query.query.startswith('c ') and len(query.query.split()) == 2)
# def query_champ_basic(q):
#     cid = q.id
#     if is_beta(cid):
#         try:
#             to_send = list()
#             c_name = q.query.split()[1].lower()
#             r = types.InlineQueryResultArticle("1", c_name, types.InputTextMessageContent(c_name))
#             bot.answer_inline_query(q.id, [r])
#             # print('\nC_NAME = ' + c_name)
#             # if c_name == 'wukong':
#             #     c_name = 'monkeyking'
#             # elif c_name == 'monkeyking':
#             #     c_name = 'wukong'
#             # for x in data[lang(cid)]:
#             #     if c_name == data[lang(cid)][x]['key'].lower():
#             #         champ=data[lang(cid)][x]
#             #         txt = champ_basic(data[lang(cid)][x], cid)
#             #         print('\n'+txt+'\n')
#             #         aux = types.InlineQueryResultArticle("1",
#             #                 champ['name'],
#             #                 types.InputTextMessageContent(txt,
#             #                     parse_mode="Markdown"),
#             #                 description=responses['inline_champ_d'][lang(cid)],
#             #                 thumb_url='http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_0.jpg')
#             #         to_send.append(aux)
#             # if to_send:
#             #     bot.answer_inline_query(q.id, to_send)
#         except:
#             pass

def champ_basic(chmp, cid):
    if chmp['key'] in backward:
        key = backward[chmp['key']]
        key2 = chmp['key']
    else:
        key = chmp['key']
        key2 = chmp['key']
    txt = '_' + chmp['name'] + ', ' + chmp['title'] + '_'
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
            txt += '\n⁣  /' + key + '\_' + \
                str(skin['num']) + ': ' + skin['name']
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
    txt += '\n\n' + responses['extra_info'][lang(cid)] + ' /' + key + '\_extra'
    return txt
