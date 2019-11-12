#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s datadir=/usr/share/" % get.installDIR())

    inarytools.dodoc("COPYING*", "README")
