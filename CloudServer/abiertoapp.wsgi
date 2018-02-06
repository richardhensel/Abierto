#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/Flask/")

from Abierto import app as application
application.secret_key = 'kmkjwdv8387495?*&DC'
