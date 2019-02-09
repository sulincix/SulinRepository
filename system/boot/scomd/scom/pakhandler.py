# -*- coding: utf-8 -*-

import ciksemel
import imp

def doenv(filetag):
    for item in filetag:
        path = item.getTagData("Path")
        if path.startswith("etc/env.d"):
            updenv = imp.load_source("updenv", "/sbin/update-environment")
            updenv.update_environment("/")
            return

def setupPackage(metapath, filepath):
    doc = ciksemel.parse(filepath)
    doenv(doc.tags("File"))

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    doc = ciksemel.parse(filepath)
    doenv(doc.tags("File"))
