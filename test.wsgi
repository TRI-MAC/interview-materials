import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/test/')
from test import app as application
application.secret_key = 'mac'
