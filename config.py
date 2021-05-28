#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################
#                   BOT TOKEN #
#################################################

import os
import telebot
from telebot import types
from colorclass import Color
import json
import time
import six
import sys
import traceback
import re
import socket
from collections import OrderedDict
from pymongo import MongoClient
import requests
from random import choice
import logging
import _thread

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

with open('extra_data/extra.json', 'r') as f:
    extra = json.load(f)

telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(extra['token'])
logBot = telebot.TeleBot(extra['token_logbot'])
admins = extra['admins']
filtered = list()

client = MongoClient('database:27017')
db = client.lol_bot


with open('responses.json', encoding='utf-8') as f:
    responses = json.load(f, object_pairs_hook=OrderedDict)


userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 60


def is_banned(uid):
    if is_user(uid):
        return db.users.find_one(str(uid))['banned']
    else:
        return False


def next_step_handler(uid):
    """ Función para controlar los steps dentro de las diferentes funciones """
    if uid not in userStep or is_banned(uid):
        userStep[uid] = 0
    return userStep[uid]


def lang(uid):
    if db.users.find_one(str(uid)):
        return db.users.find_one(str(uid))['lang']
    else:
        return 'en'


def is_beta(uid):
    """ Función para comprobar si un ID es beta """
    return uid in extra['beta']


def was_user(cid):
    return db.users.find_one(str(cid)) is not None and db.users.find_one(str(cid))['active'] == False


def is_user(cid):
    return db.users.find_one(str(cid)) is not None and db.users.find_one(str(cid))['active'] == True


def is_admin(cid):
    """ Función para comprobar si un ID es admin """
    return int(cid) in admins


def remove_tag(text):
    TAG_RE = re.compile(r'<[^>]+>')
    return TAG_RE.sub('', text)


def isint(s):
    if not s:
        return False
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def user_info(cid, language=None):
    from datetime import datetime
    yes = "✔️"
    no = "✖️"
    user = db.users.find_one(str(cid))
    reg_date = datetime.fromtimestamp(int(user['register'])).strftime('%d/%m/%Y')
    notifications = yes if user['notify'] else no
    summoner_name = user['summoner'] if user['summoner'] else no
    region = user['server'].upper() if user['server'] else no
    return responses['user_info'][lang(cid) if not language else language].format(reg_date, notifications, summoner_name, region) if int(cid) > 0 else responses['group_info'][lang(cid) if not language else language].format(reg_date, notifications)


def escape_markup(text):
    if not isinstance(text, str):
        return text
    characters = ['_', '*', '[']
    for character in characters:
        text = text.replace(character, '\\' + character)
    return text


def contact_format(m):
    name = m.from_user.first_name
    alias = str(m.from_user.username)
    cid = str(m.chat.id)
    uid = str(m.from_user.id)
    m_id = str(m.message_id)
    msg = m.text
    if cid == uid:
        txt = "Nuevo mensaje\n\nNombre: " + name + "\nAlias: @" + alias + "\nIdioma: " + \
            lang(cid) + "\nM_ID: " + m_id + "\nID: " + cid + "\n\nMensaje: " + msg
    else:
        txt = "Nuevo mensaje\n\nNombre: " + name + "\nAlias: @" + alias + "\nIdioma: " + lang(
            cid) + "\nM_ID: " + m_id + "\nID: " + cid + "\nUID: " + uid + "\n\nMensaje: " + msg
    return txt

with open('extra_data/file_ids.json', 'r') as f:
    file_ids = json.load(f)

with open('extra_data/sorcio.json', 'r') as f:
    sorcio = json.load(f)

data = dict()

for x in [
    'es',
    'en',
    'de',
    'it',
    'fr',
    'pl',
    'pt',
    'ru',
    'el',
    'th',
    'tr',
        'ro']:
    with open('champs_%s.json' % x, 'r') as f:
        data[x] = json.load(f)

with open('champs_en.json', 'r') as f:
    data['fa'] = data['ar'] = json.load(f)

with open('champs_keys.json', 'r') as f:
    data['keys'] = json.load(f)


def line(alt=False):
    if alt:
        return u'\n—————————————————————————\n'
    else:
        return u'\n`—————————————————————————`\n'


def send_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = traceback.extract_tb(exc_tb, 4)
    message = '\n`' + str(exc_type) + '`'
    message += '\n\n`' + str(exc_obj) + '`'
    for row in tb:
        message += line()
        for val in row:
            message += '`' + str(val) + '`\n'
    return message


def to_json(m):
    d = {}
    for x, y in six.iteritems(m.__dict__):
        if hasattr(y, '__dict__'):
            d[x] = to_json(y)
        else:
            d[x] = y
    return d


def get_static_version():
    return extra['static_version']

def set_static_version(static_version):
    extra['static_version'] = static_version
    with open('extra_data/extra.json', 'w') as f:
        json.dump(extra, f, indent=4)


base_regions = {'euw': 'euw1',
                'ru': 'ru',
                'kr': 'kr',
                'br': 'br1',
                'oce': 'oc1',
                'na': 'na1',
                'eune': 'eun1',
                'lan': 'la1',
                'las': 'la2',
                'tr': 'tr1'}


def update_region(reg):
    return base_regions.get(reg)


def get_3_best_champs(summonerId, region, cid):
    url = 'https://{}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}'.format(
        update_region(region.lower()), summonerId)
    params = {
        "api_key": extra['lol_api']
    }
    jstr = requests.get(
        url=url,
        params=params
    )
    if jstr.status_code != 200:
        return None
    else:
        return OrderedDict([(data[lang(cid)][data['keys'][str(x['championId'])]['key']][
                           'name'], str(x['championLevel'])) for x in jstr.json()[:3]])


def get_summoner(name, region, mode='lol'):
    if mode == 'tft':
        url = f'https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{name}'
    else:
        url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'
    params = {
        'api_key': extra['tft_api'] if mode == 'tft' else extra['lol_api']
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception(f"Error finding {name} in {region}")
    return r.json()


def get_matches_id_tft(puuid, region, count=5):
    url = f'https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids'
    params = {
        'api_key': extra['tft_api'],
        'count': count
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception(f"Error finding matches for {puuid} in {region}")
    return r.json()


def get_matches_id_lol(accountId, region, count=5):
    url = f'https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}'
    params = {
        'api_key': extra['lol_api'],
        'endIndex': count
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception(f"Error finding matches for {accountId} in {region}")
    return r.json()


def get_matches_id(puuid, region, mode='lol', count=5):
    if mode == 'tft':
        url = f'https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids'
    else:
        url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids'
    params = {
        'api_key': extra['tft_api'] if mode == 'tft' else extra['lol_api'],
        'count': count
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception(f"Error finding matches for {puuid} in {region}")
    return r.json()


def process_match(puuid, region, match_id, mode = 'lol'):
    if mode == 'tft':
        url = f'https://{region}.api.riotgames.com/tft/match/v1/matches/{match_id}'
    else:
        url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}'
    params = {
        'api_key': extra['tft_api'] if mode == 'tft' else extra['lol_api']
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception(f"Error finding match {puuid}")
    match = r.json()
    output = {}
    if mode == 'tft':
        output = [x for x in match['info']['participants'] if x['puuid'] == puuid][0]
    else:
        output = {
            'game_mode': match['info']['gameMode'],
            'summoner': [x for x in match['info']['participants'] if x['puuid'] == puuid][0]
        }
    return output


def get_rank_info(summoner_id, region, mode='lol'):
    if mode == 'tft':
        url = f'https://{region}.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}'
    else:
        url = f'https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
    output = {}
    params = {
        'api_key': extra['tft_api'] if mode == 'tft' else extra['lol_api']
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        output = {'error': 'Error cargando información del jugador'}
        return output
    r_json = r.json()
    if len(r_json) == 1:
        output = {r_json[0]['queueType']:r_json[0]}
    else:
        output = {x['queueType']:x for x in r_json}
    return output


def get_summoner_info(invocador, region, cid):
    try:
        summoner_lol = get_summoner(invocador, update_region(region))
        summoner_tft = get_summoner(invocador, update_region(region), 'tft')
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    lattest_version = get_static_version()
    icon_id = summoner_lol['profileIconId']
    icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
        lattest_version, icon_id)
    summoner_name = summoner_lol['name']
    opgg_region = region.lower() if region.lower() != 'kr' else 'www'
    opgg = 'http://{}.op.gg/summoner/userName={}'.format(opgg_region, ''.join(summoner_name.split()))
    # lolking = "http://www.lolking.net/summoner/" + \
    #     region + "/" + str(summoner_id)
    summoner_level = summoner_lol['summonerLevel']
    txt = responses['summoner_30_beta_1'][lang(cid)].format(icon_url, summoner_name, opgg, summoner_level)
    if summoner_level > 29:
        rank_lol = get_rank_info(summoner_lol['id'], update_region(region), 'lol')
        rank_tft = get_rank_info(summoner_tft['id'], update_region(region), 'tft')
        # Información de partidas LOL
        for x in rank_lol:
            txt += responses['summoner_30_beta_2'][lang(cid)].format(
                        "SoloQ" if x == "RANKED_SOLO_5x5" else "FlexQ" if x == "RANKED_FLEX_SR" else x,
                        responses['tier'][lang(cid)][rank_lol[x]['tier']],
                        rank_lol[x]['rank'],
                        rank_lol[x]['wins'],
                        rank_lol[x]['losses'],
                        rank_lol[x]['leaguePoints'])

        # Información de partidas TFT
        for x in rank_tft:
            txt += responses['summoner_30_beta_2'][lang(cid)].format(
                        "Ranked TFT" if x == "RANKED_TFT" else x,
                        responses['tier'][lang(cid)][rank_tft[x]['tier']],
                        rank_tft[x]['rank'],
                        rank_tft[x]['wins'],
                        rank_tft[x]['losses'],
                        rank_tft[x]['leaguePoints'])
        try:
            bst = get_3_best_champs(summoner_lol['id'], region, cid)
            if bst:
                txt += '\n\n*' + responses['best_champs'][lang(cid)] + '*:'
                for x, y in bst.items():
                    txt += '\n- ' + x + ' _(Level: ' + y + ')_'
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    return txt

def restart_process():
     _thread.interrupt_main()
