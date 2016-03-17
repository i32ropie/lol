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
import socket
from collections import OrderedDict
from pymongo import MongoClient

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
sock = socket.socket(socket.AF_INET,
             socket.SOCK_DGRAM)
MESSAGE = extra['udp_message']
UDP_IP = extra['udp_ip']
UDP_PORT = extra['udp_port']

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
    "zewi": "Fanático de lo sensual",
    "hernando": "vinicius",
    "programame esta": "`#include <iostream>\n\nvoid main(){\n    std::cout << \"Prográmame esta\" << std::endl;\n}`"
}


client = MongoClient('localhost:27017')
db = client.users


with open('responses.json') as f:
    responses = json.load(f, object_pairs_hook=OrderedDict)


def send_udp():
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))


userStep = dict()


def is_recent(m):
    return (time.time() - m.date) < 5


def next_step_handler(uid):
    """ Función para controlar los steps dentro de las diferentes funciones """
    if uid not in userStep:
        userStep[uid] = 0
    return userStep[uid]


def lang(uid):
    return db.usuarios.find_one(str(uid))['lang']


def log(cid, msg):
    """ Función que guarda un mensaje en el archivo de log """
    with open('logs/log.' + str(cid) + '.txt', 'a') as f:
        f.write(msg)


def is_banned(uid):
    if is_user(uid):
        return db.usuarios.find_one(str(uid))['banned']
    else:
        return False


def is_beta(uid):
    """ Función para comprobar si un ID es beta """
    return uid in extra['beta']


def is_user(cid):
    return db.usuarios.find_one(str(cid)) != None


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
