#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Süleyman POYRAZ (Zaryob)
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.configure("--enable-locking \
                         --disable-root-passwd \
                         --with-x-app-defaults=/usr/share/X11/app-defaults \
                         --with-dpms-ext \
                         --with-xinerama-ext \
                         --with-xf86vmode-ext \
                         --with-xf86gamma-ext \
                         --with-randr-ext \
                         --with-proc-interrupts \
                         --with-pam \
                         --without-kerberos \
                         --without-shadow \
                         --without-passwd-helper \
                         --without-login-manager \
                         --with-gtk \
                         --without-motif \
                         --with-gl \
                         --with-gle \
                         --without-pixbuf \
                         --with-xpm \
                         --with-jpeg \
                         --with-xshm-ext \
                         --with-xdbe-ext \
                         --without-readdisplay \
                         --with-browser=xdg-open \
                         --without-setuid-hacks")

def build():
    autotools.make()

def install():
    inarytools.dodir("/etc/pam.d")

    autotools.rawInstall("install_prefix=%s" % get.installDIR())

    # Remove webcollage its pr0n enabled
    inarytools.remove("/usr/libexec/xscreensaver/webcollage")
    inarytools.remove("/usr/share/man/man6/webcollage.*")
    inarytools.remove("/usr/share/xscreensaver/config/webcollage.xml")