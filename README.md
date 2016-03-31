# {{ project_name }}

## Getting Started

En producción

```
sudo apt-get install libmysqlclient-dev libjpeg-dev git-core
git clone https://github.com/Etxea/pantallaseide.git
cd pantallaseide
virtualenv .
source ./bin/activate
pip install -r requirements.txt
vim pantallaseide/local_settings.py
./manage.py migrate
./manage.py loaddata sites
./manage.py collectstatic
chown www-data:www-data . -R
```

Añadir las directivas a apache

```
WSGIScriptAlias / /var/www/vhosts/eide.es/pantallaseide/pantallaseide/wsgi.py
Alias /site_media/static /var/www/vhosts/eide.es/pantallaseide/pantallaseide/site_media/static
Alias /site_media/media /var/www/vhosts/eide.es/pantallaseide/pantallaseide/site_media/media
```
