#!c:\users\thomas\documents\development\twiliosurvey\web-server\vizeserver\vize_lambda\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==35.0.1','console_scripts','easy_install-3.5'
__requires__ = 'setuptools==35.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==35.0.1', 'console_scripts', 'easy_install-3.5')()
    )
