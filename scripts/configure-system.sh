#!/bin/bash

## system update
sudo apt update &
sudo apt upgrade
sleep 60

sudo apt install libpq-dev python3-dev
sleep 60

## python dependencies
yes | sudo apt install python3-pip &
yes | sudo apt install nginx &

yes | python3 -m pip install --upgrade pip
yes | apt install python3.10-venv

## clone project
python3 -m venv venv

## activate env
source venv/bin/activate

## disable env
deactivate

## django dependencies
## python3 -m pip install requirements.txt

## run application
## gunicorn --bind 0.0.0.0:8000 core.wsgi