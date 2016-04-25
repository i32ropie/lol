# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  inline_help.py importado.{/cyan}'))

@bot.inline_handler(lambda query: query.query.lower() == 'help')
def query_help(q):
    cid = q.from_user.id
    if is_beta(cid):
        if is_banned(cid):
            return None
        txt = responses['inline_help_1'][lang(cid)]
        for x,y in responses['inline_help_2'][lang(cid)].items():
            txt += '\n`@League_of_Legends_bot ' + x + y
        aux = types.InlineQueryResultArticle('1',
                responses['inline_help_t'][lang(cid)],
                types.InputTextMessageContent(txt, parse_mode="Markdown"),
                description=responses['help_2'][lang(cid)]['inline'],
                thumb_url='http://i.imgur.com/IRTLKz4.jpg')
        bot.answer_inline_query(q.id, [aux])
