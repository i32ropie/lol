# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  inline_skins.py importado.{/cyan}'))


@bot.inline_handler(lambda query: query.query.startswith('s ') and len(query.query.split()) == 2)
def query_info(q):
    cid = q.from_user.id
    if is_beta(cid):
        try:
            to_send=list()
            c_name=q.query.split()[1].lower()
            for x in data[lang(cid)]:
                if c_name == data[lang(cid)][x]['key'].lower():
                    champ=data[lang(cid)][x]
                    for i in champ['skins']:
                        aux = types.InlineQueryResultPhoto(str(champ['skins'].index(i)),
                            'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_'+str(i['num'])+'.jpg',
                            'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+champ['key']+'_'+str(i['num'])+'.jpg'
                            )
                        to_send.append(aux)
            if to_send:
                bot.answer_inline_query(q.id, to_send)
        except:
            pass


@bot.message_handler(func=lambda message: message.text ==
                     "ESPAÑOL" or message.text == "INGLES")
@bot.message_handler(commands=['comando'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('comando')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        # Comando
    else:
        bot.send_message(cid, responses['not_user'])
