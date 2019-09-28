#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def setup():
    autotools.configure("--enable-shared=yes \
                         --enable-debug=no \
                         --enable-samples=no")

def build():
    autotools.make()


def install():
    autotools.install()

    inarytools.dodoc("Changes.txt", "License.txt")
