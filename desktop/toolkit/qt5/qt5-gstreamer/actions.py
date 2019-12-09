#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import kde

def setup():
    kde.configure("-DQTGSTREAMER_EXAMPLES=OFF \
                   -DQT_VERSION=5")

def build():
    kde.make()

def install():
    kde.install()

    inarytools.dodoc("COPYING", "README", "NEWS")