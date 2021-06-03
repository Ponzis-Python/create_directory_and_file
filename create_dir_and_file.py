#!/usr/bin/env python

import os, errno
import sys
from pathlib import Path

if os.geteuid() != 0:
    os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

try:
    daDir = input("Paste new subdirectory name after ponzi here: ")
    os.makedirs('/var/log/updates/ponzi/{}'.format(daDir))
    os.chmod('/var/log/updates/ponzi/{}'.format(daDir), 0o775)
    Path('/var/log/updates/ponzi/{}'.format(daDir) + '/' + 'foo.log').touch()
    os.chmod('/var/log/updates/ponzi/{}'.format(daDir) + '/' + 'foo.log+', 0o777)

except OSError as e:
    if e.errno != errno.EEXIST:
        raise
