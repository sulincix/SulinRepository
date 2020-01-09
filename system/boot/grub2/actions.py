#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

WorkDir="grub-%s" % (get.srcVERSION().replace("_", "~"))

def setup():

    shelltools.copy("../unifont*.bdf", "./unifont.bdf")
    shelltools.export("GRUB_CONTRIB", "%s/grub-2.04/grub-extras" % (get.workDIR()))

    inarytools.cflags.remove("-fstack-protector", "-fasynchronous-unwind-tables", "-fexceptions", "-fPIC")
    inarytools.cflags.sub("\s?(-O[\ds]|-D_FORTIFY_SOURCE=\d)\s?", " ")

#    shelltools.system("./linguas.sh")
    shelltools.system("./autogen.sh")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --disable-werror \
                         --with-grubdir=grub2 \
                         --program-transform-name='s,grub,grub2,'\
                         --program-prefix= \
                         --enable-grub-mkfont \
                         --enable-grub-mount \
                         --with-platform=pc \
                         --target='i386' \
                         --htmldir='/usr/share/doc/grub2/html' ")


    shelltools.copytree("../grub-%s" % (get.srcVERSION().replace("_", "~")), "../grub-%s-efi" % get.srcVERSION())
    shelltools.cd("../grub-%s-efi" % get.srcVERSION())
    shelltools.system("./autogen.sh")
    autotools.configure("PYTHON=/usr/bin/python3 \
                         --disable-werror \
                         --with-grubdir=grub2 \
                         --program-transform-name='s,grub,grub2,'\
                         --program-prefix= \
                         --enable-grub-mkfont \
                         --enable-grub-mount \
                         --with-platform=efi \
                         --target=x86_64  \
                         --htmldir='/usr/share/doc/grub2/html' ")


    shelltools.cd("..")


def build():
    #make-dist for creating all updated translation files
    #autotools.make("dist")
    autotools.make()

    shelltools.cd("../grub-%s-efi" % get.srcVERSION())
    autotools.make()
    shelltools.cd("..")

def install():
    # Install unicode.pf2 using downloaded font source.
    shelltools.system("./grub-mkfont -o unicode.pf2 unifont.bdf")

    # Create directory for grub.cfg file
    inarytools.dodir("/boot/grub2")

    inarytools.insinto("/boot/grub2", "unicode.pf2")

    #remove -r 0x0-0x7F entries to fix ugly fonts or find a suitable range parameter -r ***
    shelltools.system("./grub-mkfont -o DejaVuSans-10.pf2 -r 0x0-0x7F -s 10 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-12.pf2 -r 0x0-0x7F -s 12 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-16.pf2 -r 0x0-0x7F -s 16 /usr/share/fonts/dejavu/DejaVuSans.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-Bold-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf")
    shelltools.system("./grub-mkfont -o DejaVuSans-Mono-14.pf2 -r 0x0-0x7F -s 14 /usr/share/fonts/dejavu/DejaVuSansMono.ttf")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("ABOUT-NLS", "AUTHORS", "BUGS", "ChangeLog", "COPYING", "TODO", "README")

    shelltools.cd("../grub-%s-efi" % get.srcVERSION())

    autotools.rawInstall("DESTDIR=%s/efi" % get.installDIR())


    shelltools.copytree("/%s/efi/usr/lib/grub/x86_64-efi" % get.installDIR(), "%s/usr/lib/grub/x86_64-efi" % get.installDIR())
    inarytools.removeDir("/efi")
