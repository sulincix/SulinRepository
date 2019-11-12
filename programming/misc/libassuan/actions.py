#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIC -DPIC" % get.CFLAGS())
    shelltools.export("LDFLAGS","%s -fPIC" % get.LDFLAGS())

    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
