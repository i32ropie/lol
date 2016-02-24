# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))

helper = {
    "champs_es.json": "es",
    "champs_en.json": "en",
    "champs_it.json": "it",
    "champs_de.json": "de",
    "champs_fr.json": "fr",
    "champs_pl.json": "pl",
    "champs_pt.json": "pt",
    "champs_el.json": "el",
    "champs_ru.json": "ru",
    "champs_th.json": "th"
}

@bot.message_handler(commands=['update_champs'])
def command_update_champs(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/update_champs"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_message(
            cid, "Descargando nuevas bases de datos de campeones...")
        try:
            data['es'] = lol_api.static_get_champion_list(
                region='euw',
                locale='es_ES',
                champ_data=['all'],
                data_by_id=False)['data']
            data['en'] = lol_api.static_get_champion_list(
                region='euw',
                locale='en_US',
                champ_data=['all'],
                data_by_id=False)['data']
            data['it'] = lol_api.static_get_champion_list(
                region='euw',
                locale='it_IT',
                champ_data=['all'],
                data_by_id=False)['data']
            data['de'] = lol_api.static_get_champion_list(
                region='euw',
                locale='de_DE',
                champ_data=['all'],
                data_by_id=False)['data']
            data['fr'] = lol_api.static_get_champion_list(
                region='euw',
                locale='fr_FR',
                champ_data=['all'],
                data_by_id=False)['data']
            data['pl'] = lol_api.static_get_champion_list(
                region='euw',
                locale='pl_PL',
                champ_data=['all'],
                data_by_id=False)['data']
            data['pt'] = lol_api.static_get_champion_list(
                region='euw',
                locale='pt_BR',
                champ_data=['all'],
                data_by_id=False)['data']
            data['el'] = lol_api.static_get_champion_list(
                region='euw',
                locale='el_GR',
                champ_data=['all'],
                data_by_id=False)['data']
            data['ru'] = lol_api.static_get_champion_list(
                region='euw',
                locale='ru_RU',
                champ_data=['all'],
                data_by_id=False)['data']
            data['th'] = lol_api.static_get_champion_list(
                region='euw',
                locale='th_TH',
                champ_data=['all'],
                data_by_id=False)['data']
        except:
            bot.send_message(cid, "Error descargando nuevas bases de datos.")
            return
        bot.send_message(cid, "Bases de datos descargadas.")
        bot.send_message(cid, "Actualizando archivos...")
        try:
            for x in helper:
                with open(x, 'w') as f:
                    json.dump(data[helper[x]], f)
        except:
            bot.send_message(cid, "Error actualizando archivos.")
            return
        bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.send_message(cid, "Reiniciando bot...")
        exit()
