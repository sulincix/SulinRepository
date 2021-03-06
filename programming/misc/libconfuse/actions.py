#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir="confuse-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-static=no \
                         --enable-shared=yes \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "README", "NEWS")

    inarytools.doman("doc/man/man3/*")
