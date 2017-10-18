import logging

#Config
MYSQL_HOST = '103.76.104.245'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'tienon'
MYSQL_DB = 'shadowsocks'

MANAGE_PASS = 'passwd'
#if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
#make sure this port is idle
MANAGE_PORT = 23333

PANEL_VERSION = 'V3' # V2 or V3. V2 not support API
API_URL = 'https://speedss.ml/mu'
API_PASS = 'tienon'
NODE_ID = '6'
CHECKTIME = 60
SYNCTIME = 300

#BIND IP
#if you want bind ipv4 and ipv6 '[::]'
#if you want bind all of ipv4 if '0.0.0.0'
#if you want bind all of if only '4.4.4.4'
SS_BIND_IP = '0.0.0.0'
SS_METHOD = 'aes-256-cfb'

#LOG CONFIG
LOG_ENABLE = True
LOG_LEVEL = logging.INFO
LOG_FILE = '/var/log/shadowsocks-rm.log'

