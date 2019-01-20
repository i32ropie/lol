# -*- coding: utf-8 -*-

from config import *
import requests

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))


@bot.message_handler(commands=['update_champs'])
def command_update_champs(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        if(len(m.text.split()) != 2):
            return bot.send_message(cid, responses['update_champs_no_version'], parse_mode="Markdown")
        version = m.text.split(None, 1)[1]
        file_name = 'dragontail-{}.tgz'.format(version)
        bot.send_message(cid, responses['update_champs_1'].format(file_name))
        os.popen('wget -q https://ddragon.leagueoflegends.com/cdn/{}'.format(file_name)).read()
        try:
            os.mkdir('tmp')
        except:
            pass
        bot.send_message(cid, responses['update_champs_2'])
        os.popen('tar -xvf {} -C tmp/'.format(file_name)).read()
        bot.send_message(cid, responses['update_champs_3'])
        with open('champs_es.json', 'w') as f:
            with open('tmp/{}/data/es_ES/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            aux_2 = {y['key']:{'id':int(y['key']), 'key': y['id'], 'name': y['name']} for x, y in aux.items()}
            with open('champs_keys.json', 'w') as j:
                json.dump(aux_2, j, indent=4)
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_en.json', 'w') as f:
            with open('tmp/{}/data/en_US/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_it.json', 'w') as f:
            with open('tmp/{}/data/it_IT/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_de.json', 'w') as f:
            with open('tmp/{}/data/de_DE/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_fr.json', 'w') as f:
            with open('tmp/{}/data/fr_FR/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_ro.json', 'w') as f:
            with open('tmp/{}/data/ro_RO/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_pl.json', 'w') as f:
            with open('tmp/{}/data/pl_PL/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_pt.json', 'w') as f:
            with open('tmp/{}/data/pt_BR/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_el.json', 'w') as f:
            with open('tmp/{}/data/el_GR/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_ru.json', 'w') as f:
            with open('tmp/{}/data/ru_RU/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_th.json', 'w') as f:
            with open('tmp/{}/data/th_TH/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        with open('champs_tr.json', 'w') as f:
            with open('tmp/{}/data/tr_TR/championFull.json'.format(version)) as z:
                aux = json.load(z)['data']
            for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
            json.dump(aux, f, indent=4)
        bot.send_message(cid, responses['update_champs_4'])
        os.popen('rm -rf tmp/ {}'.format(file_name)).read()
        os.popen('pm2 restart LCS_bot')