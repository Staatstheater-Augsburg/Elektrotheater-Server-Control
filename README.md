# Installation


## Clone repository

    git clone --recursive https://github.com/Staatstheater-Augsburg/VR-Hub-Server-Control.git


## Create a Python environment

    python3 -m venv venv
    . venv/bin/activate


## Install flask and dependencies

    pip install --upgrade pip
    pip install Flask Flask-HTTPAuth python-dotenv


## Create a user

The app uses basic HTTP authentication and looks for credentials in a .env file.
So first you need to create one using the provided script:

    python create_user.py

The script will ask for your username and passwoird and generate hash.
Create a new file `.env`and copy the script output in there.


## Run development

    python app.py


# Development

## Watch and compile SASS files

    sass --watch --style compressed styles.scss styles.css


# Production


## Install server

Create directory

    sudo mkdir /opt/vr-theater-server-control
    sudo chown YOUR_USER:YOUR_USER /opt/vr-theater-server-control

Install as described above


## Create system service

Copy `.service` to

    /usr/lib/systemd/system/vr-theater-server-control.service

Enable

    sudo systemctl enable vr-theater-server-control

Start

    sudo systemctl start vr-theater-server-control