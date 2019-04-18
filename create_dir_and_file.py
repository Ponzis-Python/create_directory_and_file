import os, errno
import sys
from pathlib import Path
#Allows creation of subdirectory and file in root directories,
#without running program with sudo

fuddit = (os.path.isdir("/var/log/updates/ponzi/foo"))

if fuddit==False:
    if os.geteuid() != 0:
        os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

    try:
        os.makedirs('/var/log/updates/ponzi/foo')
        os.chmod('/var/log/updates/ponzi/foo', 0o755)
        Path('/var/log/updates/ponzi/foo/dafoofoo.txt').touch()
        os.chmod('/var/log/updates/ponzi/foo/dafoofoo.txt', 0o777)

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
else:
    print("directory exists")