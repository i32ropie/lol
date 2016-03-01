#################################################
#                   BOT TOKEN                   #
#################################################

import os
import telebot
from riotwatcher import RiotWatcher, player_stat_summary_types
from telebot import types
from colorclass import Color
import json
import time
import six
import botan
import sys
import traceback
import re
from collections import OrderedDict

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

with open('extra_data/extra.json', 'r') as f:
    extra = json.load(f)

bot = telebot.TeleBot(extra['token'])
logBot = telebot.TeleBot(extra['token_logbot'])
botan_token = extra['botan_token']
lol_api = RiotWatcher(extra['lol_api'])

admins = extra['admins']

easter_eggs = {
    "edu": "`smellz`",
    "raina": "🌧🌧🌧",
    "rapsodas": "rapsidas",
    "alin": "nigro",
    "abu": "matas",
    "vir": "igriv",
    "igriv": "vir",
    "loma": "Best streamer EUW: http://www.twitch.tv/lomavid",
    "lomavid": "Best streamer EUW: http://www.twitch.tv/lomavid",
    "lomadien": "Best streamer EUW: http://www.twitch.tv/lomavid",
    "mega": "flipetis",
    "putaama": "xeha",
    "xeha": "putaama",
    "zewi": "Fanático de lo homosexual",
    "hernando": "vinicius",
    "programame esta": "`#include <iostream>\n\nvoid main(){\n    std::cout << \"Programame esta\" << std::endl;\n}`"
}

with open('usuarios.json') as f:
    users = json.load(f)

with open('responses.json') as f:
    responses = json.load(f, object_pairs_hook=OrderedDict)

with open('twitch.json') as f:
    twitch_users = json.load(f)

userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 5


def next_step_handler(uid):
    """ Función para controlar los steps dentro de las diferentes funciones """
    if uid not in userStep:
        userStep[uid] = 0
    return userStep[uid]


def lang(uid):
    """ Función que devuelve el idioma del usuario """
    return users[str(uid)]['lang']


def log(cid, msg):
    """ Función que guarda un mensaje en el archivo de log """
    with open('logs/log.' + str(cid) + '.txt', 'a') as f:
        f.write(msg)


def is_banned(uid):
    """ Función para comprobar si un ID está baneado """
    if str(uid) in users:
        return users[str(uid)]['banned']
    else:
        return False


def is_beta(uid):
    """ Función para comprobar si un ID es beta """
    return uid in extra['beta']


def is_user(cid):
    """ Función para comprobar si un ID es usuario """
    return str(cid) in users


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
    msg = m.text
    if cid == uid:
        txt = "*Nuevo mensaje\n\nNombre*: _" + escape_markup(name) + "_\n*Alias*: _@" + alias + "_\n*Idioma*: _" + lang(
            cid) + "_\n*ID*: _" + cid + "_\n\n*Mensaje*: _" + escape_markup(msg) + "_"
    else:
        txt = "*Nuevo mensaje\n\nNombre*: _" + escape_markup(name) + "_\n*Alias*: _@" + alias + "_\n*Idioma*: _" + lang(
            cid) + "_\n*ID*: _" + cid + "_\n*UID*: _" + uid + "_\n\n*Mensaje*: _" + escape_markup(msg) + "_"
    return txt

with open('extra_data/file_ids.json', 'r') as f:
    file_ids = json.load(f)

data = dict()

for x in ['es', 'en', 'de', 'it', 'fr', 'pl', 'pt','ru','el','th']:
    with open('champs_%s.json' % x, 'r') as f:
        data[x] = json.load(f)

with open('champs_en.json', 'r') as f:
    data['fa'] = json.load(f)

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
# champs_es = lol_api.static_get_champion_list(region='euw', locale='es_ES', champ_data=['all'], data_by_id=False)['data']
