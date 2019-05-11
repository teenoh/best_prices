
"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/teenoh/.virtualenvs/best_prices_venv/lib/python3.5/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

activate_this = os.path.expanduser("~/.virtualenvs/best_prices_venv/bin/activate_this.py")

exec(open(activate_this).read())
project = '/home/teenoh/webapps/best_prices/best_prices/best_prices_api/server/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
