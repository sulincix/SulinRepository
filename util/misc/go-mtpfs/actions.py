#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools

def install():
    inarytools.insinto("/usr/lib/go/src/pkg", "fs")
    inarytools.insinto("/usr/lib/go/src/pkg", "mtp")

    inarytools.dodoc("LICENSE")

