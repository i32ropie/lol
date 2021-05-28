# -*- coding: utf-8 -*-

from config import *
import requests

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))


@bot.message_handler(commands=['update_champs'])
def command_update_champs(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        if(len(m.text.split()) != 2):
            return bot.send_message(cid, responses['update_champs_no_version'], parse_mode="Markdown")
        version = m.text.split(None, 1)[1]
        langs = ['es_ES', 'en_US', 'it_IT', 'de_DE', 'fr_FR', 'ro_RO', 'pl_PL', 'pt_BR', 'el_GR', 'ru_RU', 'th_TH', 'tr_TR']
        url = 'http://ddragon.leagueoflegends.com/cdn/{}/data/{}/championFull.json'
        splash = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/{}_{}.jpg'

        for z in langs:
            bot.send_message(cid, "Consultando información para el idioma '{}'".format(z))
            r = requests.get(url.format(version, z))
            if r.status_code == 200:
                aux = r.json()['data']
                for x, y in aux.items(): y['key'], y['id'] = y['id'], int(y['key'])
                with open('champs_{}.json'.format(z.split("_")[0]), 'w') as f:
                    json.dump(aux, f, indent=4)
            else:
                bot.send_message(cid, "No se ha conseguido extraer información de la URL {}".format(url.format(version, z)))

        bot.send_message(cid, "Generando champs_keys.json")
        r = requests.get(url.format(version, langs[0]))
        if r.status_code == 200:
            aux = r.json()['data']
            aux_2 = {y['key']:{'id':int(y['key']), 'key': y['id'], 'name': y['name']} for _, y in aux.items()}
            with open('champs_keys.json', 'w') as f:
                json.dump(aux_2, f, indent=4)
        else:
            bot.send_message(cid, "No se ha conseguido extraer información de la URL {}".format(url.format(version, langs[0])))

        with open('champs_es.json') as f:
            champs = json.load(f)

        with open('extra_data/file_ids.json') as f:
            file_ids = json.load(f)

        for x, y in champs.items():
            print('Campeón cargado: {}'.format(x))
            for z in [z.get('num') for z in y.get('skins')]:
                clave = x.lower()
                if clave == 'monkeyking':
                    clave = 'wukong'
                if z != 0:
                    clave += '_{}'.format(z)
                if file_ids.get(clave) is None:
                    print('\tObteniendo la siguiente imagen: {}'.format(splash.format(x, z)))
                    r = requests.get(splash.format(x, z))
                    if r.status_code != 200:
                        print('\t\tERROR, status_code = {}'.format(r.status_code))
                        continue
                    msg = bot.send_photo(52033876, r.content)
                    valor = msg.photo[-1].file_id
                    file_ids[clave] = valor
        bot.send_message(cid, "Hemos terminado de actualizar las imágenes, actualizamos el fichero de file_ids")
        with open('extra_data/file_ids.json', 'w') as f:
            json.dump(file_ids, f, indent=2, sort_keys=True)
        bot.send_message(cid, "Actualizado fichero de file_ids. Actualizamos ahora la configuración con la versión de estáticos")
        set_static_version(version)
        bot.send_message(cid, "Actualizada versión estática, reiniciamos")
        restart_process()
