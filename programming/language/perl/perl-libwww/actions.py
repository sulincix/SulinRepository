#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import perlmodules
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "libwww-perl-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def check():
    perlmodules.make("test")

def install():
    perlmodules.install()
    for method in ["GET", "POST", "HEAD"]:
        inarytools.dosym("/usr/bin/lwp-request", "/usr/bin/%s" % method)

    inarytools.dodoc("Changes","README")
