from django.core.wsgi import get_wsgi_application
"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/teenoh/.virtualenvs/mino/lib/python3.5/site-packages')
activate_this = os.path.expanduser("~/.virtualenvs/mino/bin/activate_this.py")
exec(open(activate_this).read())
project = '/home/teenoh/webapps/minomain/mino/'
workspace = os.path.dirname(project)
sys.path.append(workspace)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
