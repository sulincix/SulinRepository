#!/usr/bin/env python3

import os

def postInstall():
    os.system("/bin/chown -R postgres:postgres /var/lib/postgresql")
    os.system("/bin/chmod -R 0700 /var/lib/postgresql/data")
    os.system("/bin/chmod -R 0700 /var/lib/postgresql/backups")

    # On first install...
    if not os.path.exists("/var/lib/postgresql/data/base"):
        for i in ["LANG", "LANGUAGE", "LC_ALL"]:
            os.environ[i] = "en_US.UTF-8"

        os.system('/bin/su postgres -s /bin/sh -p -c "/usr/bin/initdb --pgdata /var/lib/postgresql/data"')
