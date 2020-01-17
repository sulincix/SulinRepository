# -*- coding: utf-8 -*-
serviceType = "server"
serviceDesc = {"en": "RSync Daemon",
               "tr": "RSync Servisi"}
serviceConf = "rsyncd"

from scom.service import *

@synchronized
def start():
    startService(command="/usr/bin/rsync",
                 args="--daemon %s" % config.get("RSYNC_OPTS", ""),
                 pidfile="/run/rsyncd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/run/rsyncd.pid",
                donotify=True)

def status():
    return isServiceRunning("/run/rsyncd.pid")
