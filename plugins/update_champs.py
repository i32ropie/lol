# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_champs.py importado.{/cyan}'))


@bot.message_handler(commands=['update_champs_1'])
def command_update_champs_1(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_1')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        msg = bot.send_message(
            cid, "Descargando nuevas bases de datos de campeones:\n`-Español`\n`-Inglés`\n`-Italiano`\n`-Alemán`\n`-Francés`", parse_mode="Markdown")
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
                    data_by_id=False)['data']}
        except:
            # bot.send_message(cid, "Error descargando nuevas bases de datos.")
            bot.edit_message_text("Error descargando nuevas bases de datos.", cid, msg.message_id)
            return
        # bot.send_message(cid, "Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", parse_mode="Markdown")
        bot.edit_message_text("Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", cid, msg.message_id, parse_mode="Markdown")
        # bot.send_message(cid, "Actualizando archivos...")
        bot.edit_message_text("Actualizando archivos...", cid, msg.message_id)
        try:
            for x in aux:
                with open(x, 'w') as f:
                    json.dump(aux[x], f)
        except:
            # bot.send_message(cid, "Error actualizando archivos.")
            bot.edit_message_text("Error actualizando archivos.", cid, msg.message_id)
            return

        # bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.edit_message_text("Archivos actualizados correctamente.", cid, msg.message_id)
        # bot.send_message(cid, "Reiniciando bot...")
        bot.edit_message_text("Reiniciando bot...", cid, msg.message_id)
        exit()


@bot.message_handler(commands=['update_champs_2'])
def command_update_champs_2(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_2')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        msg = bot.send_message(
            cid, "Descargando nuevas bases de datos de campeones:\n`-Polaco`\n`-Portugués`\n`-Griego`\n`-Ruso`\n`-Tailandés`", parse_mode="Markdown")
        try:
            aux = {
                "champs_pl.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='pl_PL',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_pt.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='pt_BR',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_el.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='el_GR',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_ru.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='ru_RU',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_th.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='th_TH',
                    champ_data=['all'],
                    data_by_id=False)['data'],
                "champs_tr.json": lol_api.static_get_champion_list(
                    region='euw',
                    locale='tr_TR',
                    champ_data=['all'],
                    data_by_id=False)['data']}
        except:
            # bot.send_message(cid, "Error descargando nuevas bases de datos.")
            bot.edit_message_text("Error descargando nuevas bases de datos.", cid, msg.message_id)
            return
        # bot.send_message(cid, "Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", parse_mode="Markdown")
        bot.edit_message_text("Bases de datos descargadas.\n\n`" + '\n'.join([i for i in aux]) + "`", cid, msg.message_id, parse_mode="Markdown")
        # bot.send_message(cid, "Actualizando archivos...")
        bot.edit_message_text("Actualizando archivos...", cid, msg.message_id)
        try:
            for x in aux:
                with open(x, 'w') as f:
                    json.dump(aux[x], f)
        except:
            # bot.send_message(cid, "Error actualizando archivos.")
            bot.edit_message_text("Error actualizando archivos.", cid, msg.message_id)
            return

        # bot.send_message(cid, "Archivos actualizados correctamente.")
        bot.edit_message_text("Archivos actualizados correctamente.", cid, msg.message_id)
        # bot.send_message(cid, "Reiniciando bot...")
        bot.edit_message_text("Reiniciando bot...", cid, msg.message_id)
        exit()


@bot.message_handler(commands=['update_champs_keys'])
def command_update_champs_keys(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('update_champs_2')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        msg = bot.send_message(cid, "Actualizando fichero `champs_keys.json` ...", parse_mode="Markdown")
        try:
            req = lol_api.static_get_champion_list(data_by_id=True)['data']
        except:
            bot.edit_message_text("Error descargando el fichero.", cid, msg.message_id)
            return
        with open('champs_keys.json', 'w') as f:
            json.dump(req, f)
        bot.edit_message_text("Éxito. Reiniciando bot...", cid, msg.message_id)
        exit()
