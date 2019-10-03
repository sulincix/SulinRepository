from inary.actionsapi import cmaketools
from inary.actionsapi import pythonmodules

def setup():
    cmaketools.configure('-DCMAKE_INSTALL_PREFIX="/usr" -DCMAKE_INSTALL_LIBDIR="/usr/lib"')

def build():
    pythonmodules.compile()
    pythonmodules.compile(pyVer="3")
    cmaketools.make()

def install():
    pythonmodules.install()
    pythonmodules.install(pyVer="3")
    cmaketools.install()
