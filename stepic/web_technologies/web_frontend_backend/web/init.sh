#!/usr/bin/env bash
# to remove old links
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/gunicorn.d/hello.py
# linking of required files
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
# restart of servers
sudo /etc/init.d/nginx restart
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello:wsgi_application
# to remove new links
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm -f /etc/gunicorn.d/hello.py