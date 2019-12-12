#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DBUILD_ROOT=%s" % get.installDIR())

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*")
