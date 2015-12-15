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

#################################################
#          USEFUL FUNCTIONS AND DATAS           #
#################################################

with open('extra_data/extra.json','r') as f:
    extra = json.load(f)

bot = telebot.TeleBot(extra['token'])
logBot = telebot.TeleBot(extra['token_logbot'])

lol_api = RiotWatcher(extra['lol_api'])

admins = extra['admins']

banneds = []

with open('usuarios.json') as f:
    users = json.load(f)

with open('responses.json') as f:
    responses = json.load(f)

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

def log(cid,msg):
    """ Función que guarda un mensaje en el archivo de log """
    with open( 'logs/log.' + str(cid) + '.txt', 'a') as f:
        f.write(msg)

def is_banned(uid):
    """ Función para comprobar si un ID está baneado """
    if str(uid) in users:
        return users[str(uid)]['banned']
    else:
        return False

def is_user(cid):
    """ Función para comprobar si un ID es usuario """
    return str(cid) in users

def is_admin(cid):
    """ Función para comprobar si un ID es admin """
    return int(cid) in admins

def isint(s):
    if not s:
        return False
    if s[0] in ('-', '+'):
    	return s[1:].isdigit()
    return s.isdigit()

#def upper_first(string):
    #vector = list(string)
    #vector[0] = vector[0].upper()
    #return "".join(vector)

def contact_format(m):
    name = m.from_user.first_name
    alias = str(m.from_user.username)
    cid = str(m.chat.id)
    uid = str(m.from_user.id)
    msg = m.text
    if cid == uid:
        txt = "Nuevo mensaje\n\n*Nombre*: _" + name + "_\n*Alias*: @" + alias + "\n*Idioma*: _" + lang(cid) + "_\n*ID*: _" + cid + "_\n\n*Mensaje*: _" + msg + "_"
    else:
        txt = "Nuevo mensaje\n\n*Nombre*: _" + name + "_\n*Alias*: @" + alias + "\n*Idioma*: _" + lang(cid) + "_\n*CID*: _" + cid + "_\n*UID*: _" + uid + "_\n\n*Mensaje*: _" + msg + "_"
    return txt

with open('extra_data/file_ids.json','r') as f:
    file_ids = json.load(f)

data = dict()

for x in ['es','en','de','it','fr','pl','pt']:
    with open('champs_%s.json'%x,'r') as f:
        data[x] = json.load(f)

# champs_es = lol_api.static_get_champion_list(region='euw', locale='es_ES', champ_data=['all'], data_by_id=False)['data']
