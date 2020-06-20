# -*- coding: utf-8 -*-

from config import *
import re
from bs4 import BeautifulSoup
from lxml import html
import os

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_rotation.py importado.{/cyan}'))

backward = {
    'Chogath': 'ChoGath',
    'FiddleSticks': 'Fiddlesticks',
    'Leblanc': 'LeBlanc',
    'Khazix': 'KhaZix',
    'MonkeyKing': 'Wukong'
}

@bot.message_handler(commands=['update_rotation'])
def update_rotation_auto(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp(m.text.lstrip('/').split(' ')[0].split('@')[0].lower())
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) != 2:
            return bot.send_message(cid, responses['update_rotation_no_url'], parse_mode="Markdown")
        link = m.text.split()[1]
        r = requests.get(link)
        tree = html.fromstring(r.content)
        img = tree.xpath('//a[contains(@href, "rotation")]/img/@src')
        if img:
            img = img[0]
        else:
            return bot.send_message(cid, responses['update_rotation_no_img'])
        img = bot.send_photo(cid, requests.get(img).content).photo[-1].file_id
        extra['rotation'] = img
        with open('extra_data/extra.json', 'w') as f:
            json.dump(extra, f, indent=4)
        champ_names = tree.xpath('//a[contains(@href, "/champions/")]/text()')
        champ_keys = [y['key'] for x,y in data['keys'].items() if y['name'] in champ_names]
        champ_keys = [backward[x] if x in backward else x for x in champ_keys]
        with open('extra_data/rotation.txt','w') as f:
            f.write('/{}'.format('\n/'.join(champ_keys)))
        bot.send_message(cid, responses['update_rotation_end'])
