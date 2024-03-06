#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# update package lists for upgrades
sudo apt-get update

# Install nginx
sudo apt-get install -y nginx

# start Nginx
sudo service nginx start

# create directories if they dont exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# create a simple index.html file
cat <<EOF | sudo tee /data/web_static/releases/test/index.html
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
EOF

# create a symbolic link
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

chown -R  ubuntu:ubuntu "/data/"

# Backup the original configuration file
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak

# update the Nginx configuration
echo "
    server {
        listen 80;
        listen [::]:80;

        server_name taurai.tech;

        location /hbnb_static/ {
            alias /data/web_static/current/;
        }
    }" | sudo tee /etc/nginx/sites-available/default

# restart the nginx server
sudo service nginx restart
