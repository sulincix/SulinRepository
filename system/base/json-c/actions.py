#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
    cmaketools.configure()
                         
def build():
    cmaketools.make("-j1")

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    if get.buildTYPE() == "emul32":
        inarytools.dosym("libjson-c.so","/usr/lib32/libjson-c.so.4")
    else:
        inarytools.dosym("libjson-c.so","/usr/lib/libjson-c.so.4")

    inarytools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS", "NEWS")
