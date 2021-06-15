# -*- coding: utf-8 -*-

from config import *
from lxml import html


print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_rotation.py importado.{/cyan}'))

backward = {
    'Chogath': 'ChoGath',
    'FiddleSticks': 'Fiddlesticks',
    'Leblanc': 'LeBlanc',
    'Khazix': 'KhaZix',
    'MonkeyKing': 'Wukong'
}

@bot.message_handler(commands=['update_sale'])
def update_rotation_auto(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) != 2:
            return bot.send_message(cid, responses['update_sale_no_url'], parse_mode="Markdown")
        link = m.text.split()[1]
        r = requests.get(link)
        tree = html.fromstring(r.content)
        img = tree.xpath('//a[contains(@href, "sale")]/img/@src')
        if img:
            img = img[0]
        else:
            return bot.send_message(cid, responses['update_sale_no_img'])
        img = bot.send_photo(cid, requests.get(img).content).photo[-1].file_id
        extra['sale'] = img
        with open('extra_data/extra.json', 'w') as f:
            json.dump(extra, f, indent=4)
        champ_keys = [y['key'] if y['key'] not in backward else backward[y['key']] for _,y in data['keys'].items() if y['name'] in tree.xpath('//a[contains(@href, "/champions/")]/text()')]
        champ_prices = [': ' + x.replace('-','').strip() for x in tree.xpath('//a[contains(@href, "/champions/")]/parent::li/text()') if x.strip()]
        champs = sorted(zip(champ_keys, champ_prices))
        txt = '/{}'.format('\n/'.join([''.join(x) for x in champs]))
        skins_base = [[y.strip() for y in ''.join([z.strip().replace('K/DA','KDA') for z in x.xpath('b/text()')+x.xpath('text()')]).split('/')] for x in tree.xpath('//h4') if x.xpath('@id') and x.xpath('@id')[0].isdigit()]
        skins = [': '.join([data['skins'][x[0].replace('KDA', 'K/DA').lower()], x[1]]) for x in skins_base]
        txt += '\n/{}'.format('\n/'.join(skins))
        with open('extra_data/sale.txt','w') as f:
            f.write(txt)
        bot.send_message(cid, responses['update_sale_end'])
