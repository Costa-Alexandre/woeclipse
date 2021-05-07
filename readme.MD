# Flask Website Starter Template 

This repository is a website created in the context of the Foundations of Software Engineering Course run in the spring of 2021 at CODE University of Applied Sciences, based in Berlin, Germany, but run remotely due to the pandemic. It was forked from a starter template, but everything else is my original work, unless referenced. The focus here is on having a slim, working, full-stack website which can be (relatively) easily built, tested, and deployed on Google App Engine using GitHub actions. This README assume that the reader already has a basic familiarity with a broad range of topics and technologies, so it lacks explanation. 

# Installation Instructions
This will be a quick overview of how to run this project locally. 

## Before you start... 
You should have:
- [Python 3.8.x](https://www.python.org/downloads/release/python-386/) installed on your computer
- [Git 2.28+](https://git-scm.com/download/) installed on your computer
- [PostgreSQL](https://www.postgresql.org/download/) installed on your computer

### Cloning this Repo

Clone this repository to your computer 
- Choose (or create) a working directory on your own computer and change directory into it
- Clone this repository running `git clone https://github.com/Costa-Alexandre/woeclipse.git` in that working directory.

### Get Set Up for Local Development: 

- Change directory to the recently cloned folder. This will be your root folder.
- In the terminal, create a new virtual environment (e.g. 'venv') for this project:
    
    > virtualenv venv 

- Activate your virtual environment (Windows: `source venv\Scripts\activate`; Mac and Linux: `source venv/bin/activate`)
- Download the Python modules listed in requirements.txt using pip: 

    > pip install -r requirements.txt

- Set local environment variables. Create a '.env' file on your root directory. 

    > touch .env
    > echo SECRET_KEY=mysecretpassword >> .env
    > echo DB_USER=postgres >> .env
    > echo DB_PASSWORD=mypostgrespassword >> .env
    > echo DB_HOST=localhost:5432 >> .env
    > echo DB_NAME=postgres >> .env

- Make sure to change "mypostgrespassword" to your actually postgres password. These settings are assuming you will be using the default "postgres" user and database, but you can use your own database instance and user login settings. 
- Also, feel free to change "mysecretpassword" to anything you'd like - preferably to a long random string. This is [required by Flask to use sessions](https://flask.palletsprojects.com/en/1.1.x/api/?highlight=flask%20flask%20secret_key#flask.Flask.secret_key). Run this command to quicly generate a strong SECRET KEY:

    > python -c 'import os; print(os.urandom(16))'

- ATTENTION: The exact command above will depend on your operating system and setup, but the idea is the same: call the Python executable at the command line (e.g. python or python3.8 or python3 or maybe \Python38\python on Windows). Also, from now on, everytime I refer to the command `python`, adapt for your system setup. 

### Run the Flask App: 

- You are all set to run the app. Make sure the your virtual environment is active (instructions above) and you are anywhere inside the root folder.
- Run flask using:

    > flask run

- All done! You can access the flask app in your browser either on ` http://127.0.0.1:8000/` or `http://localhost:8000`.


### 