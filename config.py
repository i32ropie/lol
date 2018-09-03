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

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

with open('extra_data/extra.json', 'r') as f:
    extra = json.load(f)

bot = telebot.TeleBot(extra['token'])
logBot = telebot.TeleBot(extra['token_logbot'])
admins = extra['admins']
filtered = list()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE = extra['udp_message']
UDP_IP = extra['udp_ip']
UDP_PORT = extra['udp_port']


client = MongoClient('localhost:27017')
db = client.users


with open('responses.json', encoding='utf-8') as f:
    responses = json.load(f, object_pairs_hook=OrderedDict)


def send_udp(txt):
    pass
    #sock.sendto(MESSAGE.format(txt).encode(), (UDP_IP, UDP_PORT))


userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 60


def is_banned(uid):
    if is_user(uid):
        return db.usuarios.find_one(str(uid))['banned']
    else:
        return False


def next_step_handler(uid):
    """ Función para controlar los steps dentro de las diferentes funciones """
    if uid not in userStep or is_banned(uid):
        userStep[uid] = 0
    return userStep[uid]


def lang(uid):
    if db.usuarios.find_one(str(uid)):
        return db.usuarios.find_one(str(uid))['lang']
    else:
        return 'en'


def is_beta(uid):
    """ Función para comprobar si un ID es beta """
    return uid in extra['beta']


def is_user(cid):
    return db.usuarios.find_one(str(cid)) is not None


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


def static_versions():
    return extra['static_version']


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
    url = 'https://{}.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/{}'.format(
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


def get_summoner(name, region):
    url = "https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}".format(region, name)
    params = {
        'api_key': extra['lol_api']
    }
    r = requests.get(url, params)
    if r.status_code != 200:
        raise Exception("Error finding {} in {}".format(name, region))
    return r.json()


def get_current_game(summoner_id, region):
    url = "https://{}.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/{}".format(region, summoner_id)
    params = {
        'api_key': extra['lol_api']
    }
    r = requests.get(url=url, params=params)
    if r.status_code != 200:
        raise Exception("The summoner with ID {} is not in game.".format(summoner_id))
    return r.json()


def get_summoner_info(invocador, region, cid):
    try:
        summoner = get_summoner(name=invocador, region=update_region(region))
    except:
        txt = responses['summoner_error'][
            lang(cid)] % (invocador, region.upper())
        return txt
    lattest_version = static_versions()
    icon_id = summoner['profileIconId']
    icon_url = "http://ddragon.leagueoflegends.com/cdn/{}/img/profileicon/{}.png".format(
        lattest_version, icon_id)
    summoner_name = summoner['name']
    summoner_id = summoner['id']
    lolking = "http://www.lolking.net/summoner/" + \
        region + "/" + str(summoner_id)
    summoner_level = summoner['summonerLevel']
    txt = responses['summoner_30_beta_1'][lang(cid)].format(icon_url, summoner_name, lolking, summoner_level)
    if summoner_level > 29:
        url = "https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}".format(update_region(region), summoner_id)
        params = {'api_key': extra['lol_api']}
        r = requests.get(url, params)
        if r.status_code != 200:
            txt = "ERROR EN LÍNEA 89 DE me.py"
            return txt
        r_json = r.json()
        if not r_json:
            aux = {}
        if len(r_json) == 1:
            aux = {r_json[0]['queueType']:r_json[0]}
        else:
            aux = {x['queueType']:x for x in r_json}
        for x in aux:
            txt += responses['summoner_30_beta_2'][lang(cid)].format(
                        "SoloQ" if x == "RANKED_SOLO_5x5" else "FlexQ" if x == "RANKED_FLEX_SR" else x,
                        responses['tier'][lang(cid)][aux[x]['tier']],
                        aux[x]['rank'],
                        aux[x]['wins'],
                        aux[x]['losses'],
                        aux[x]['leaguePoints'])
        try:
            bst = get_3_best_champs(summoner['id'], region, cid)
            if bst:
                txt += '\n\n*' + responses['best_champs'][lang(cid)] + '*:'
                for x, y in bst.items():
                    txt += '\n- ' + x + ' _(Level: ' + y + ')_'
        except Exception as e:
            bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    return txt
