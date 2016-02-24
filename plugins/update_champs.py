# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))


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
            aux = {
                "champs_es.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='es_ES',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_en.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='en_US',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_it.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='it_IT',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_de.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='de_DE',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_fr.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='fr_FR',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_pl.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='pl_PL',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_pt.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='pt_BR',
                    champ_data=['all'],
                #     data_by_id=False)['data'],
                # "champs_el.json": lol_api.static_get_champion_list(
                #     region='euw',
                #     locale='el_GR',
                #     champ_data=['all'],
                #     data_by_id=False)['data'],
                # "champs_ru.json": lol_api.static_get_champion_list(
                #     region='euw',
                #     locale='ru_RU',
                #     champ_data=['all'],
                #     data_by_id=False)['data'],
                # "champs_th.json": lol_api.static_get_champion_list(
                #     region='euw',
                #     locale='th_TH',
                #     champ_data=['all'],
                    data_by_id=False)['data']}
        except:
            bot.send_message(cid, "Error descargando nuevas bases de datos.")
            return
        bot.send_message(cid, "Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", parse_mode="Markdown")
        bot.send_message(cid, "Actualizando archivos...")
        try:
            for x in aux:
                with open(x, 'w') as f:
                    json.dump(aux[x], f)
        except:
            bot.send_message(cid, "Error actualizando archivos.")
            return
        bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.send_message(cid, "Reiniciando bot...")
        exit()
