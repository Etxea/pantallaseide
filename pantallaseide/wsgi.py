"""
WSGI config for pantallaseide project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


import os, sys

parent_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.insert(0,parent_dir)
sys.path.insert(0,os.path.join(parent_dir,'lib/python2.7/site-packages'))
sys.path.insert(0,os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#sys.path.append("/var/www/vhosts/eide.es/pantallaseide")
#sys.path.insert(0,"/var/www/vhosts/eide.es/pantallaseide/bin")
#sys.path.insert(0,"/var/www/vhosts/eide.es/pantallaseide/lib/python2.7/site-packages/django")
#sys.path.insert(0,"/var/www/vhosts/eide.es/pantallaseide/lib/python2.7/site-packages")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pantallaseide.settings")

application = get_wsgi_application()
