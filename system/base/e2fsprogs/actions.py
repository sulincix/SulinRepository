#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get


def setup():
#    autotools.autoreconf("-vif")
    autotools.rawConfigure("--prefix=/usr \
                            --sbindir=/usr/bin \
                            --libdir=/usr/lib \
                            --enable-elf-shlibs \
                            --with-root-prefix="" \
                            --enable-nls \
                            --disable-e2initrd-helper \
                            --disable-libblkid \
                            --disable-libuuid \
                            --disable-fsck \
                            --disable-uuidd \
                            --enable-symlink-install \
                            --without-included-gettext")

def build():
    autotools.make("all")

def check():
    #In chroot env. /dev should be mounted to pass all tests, that's all :)
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("install install-libs LDCONFIG=/bin/true \
                          DESTDIR=%s root_sbindir=/usr/bin root_libdir=/lib" % get.installDIR())

    inarytools.remove("/usr/share/man/man8/logsave.8")
    inarytools.dodoc("README", "RELEASE-NOTES")
