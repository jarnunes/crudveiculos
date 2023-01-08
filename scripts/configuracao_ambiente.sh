#!/bin/bash

## FONTE:
## https://www.codewithharry.com/blogpost/django-deploy-nginx-gunicorn/


# Criando o arquivo
sudo nano /etc/systemd/system/gunicorn.socket
##################################################
# COLAR CONTEÚDO ABAIXO
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
##################################################

# Criando outro arquivo
sudo nano /etc/systemd/system/gunicorn.service
##################################################

# Editar, depois Colar
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/crudveiculos
ExecStart=/home/ubuntu/crudveiculos/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          core.wsgi:application

[Install]
WantedBy=multi-user.target
##
##################################################

# Ativando
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
##################################################

# Checando
sudo systemctl status gunicorn.socket
sudo systemctl status gunicorn
curl --unix-socket /run/gunicorn.sock localhost
sudo systemctl status gunicorn
##################################################

sudo nano /etc/nginx/sites-enabled/django
##################################################

# Configurando o nginx server block
server {
    listen 80;
    server_name localhost;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/ubuntu/crudveiculos;
    }

    location /media {
        alias /home/ubuntu/crudveiculos/static/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

##################################################

sudo rm /etc/nginx/sites-enabled/default
sudo systemctl restart nginx
sudo systemctl restart gunicorn
##################################################