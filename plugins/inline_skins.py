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


@bot.inline_handler(
    lambda query: query.query.startswith('s ') and len(
        query.query.split()) == 2)
def query_skins(q):
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
            if c_name == data[lang(cid)][x]['key'].lower():
                champ = data[lang(cid)][x]
                for i in champ['skins']:
                    aux = types.InlineQueryResultPhoto(
                        str(
                            champ['skins'].index(i)),
                        'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/' +
                        champ['key'] +
                        '_' +
                        str(
                            i['num']) +
                        '.jpg',
                        'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/' +
                        champ['key'] +
                        '_' +
                        str(
                            i['num']) +
                        '.jpg',
                        caption=i['name'])
                    to_send.append(aux)
        if to_send:
            bot.answer_inline_query(q.id, to_send, cache_time=1)
    except:
        pass
