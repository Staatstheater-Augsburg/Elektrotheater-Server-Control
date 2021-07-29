# Installation

## Clone repository

    git clone --recursive https://github.com/Staatstheater-Augsburg/VR-Hub-Server-Control.git


## Create a Python environment

    python3 -m venv venv
    . venv/bin/activate

## Install flask

    pip install --upgrade pip
    pip install Flask


## Run development

    python app.py


# Development

## Watch and compile SASS files

    sass --watch --style compressed styles.scss styles.css


# Production


## Install server

Create directory

    sudo mkdir /opt/vr-theater-server-control
    sudo chown vollstock:vollstock /opt/vr-theater-server-control

Install as described above


## Create system service

Copy `.service` to

    /usr/lib/systemd/system/vr-theater-server-control.service

Enable

    sudo systemctl enable vr-theater-server-control

Start

    sudo systemctl start vr-theater-server-control