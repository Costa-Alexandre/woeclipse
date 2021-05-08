# Flask Website Starter Template 

This repository is a website created in the context of the Foundations of Software Engineering Course run in the spring of 2021 at CODE University of Applied Sciences, based in Berlin, Germany, but run remotely due to the pandemic. It was forked from a starter template, but everything else is my original work, unless referenced. The focus here is on having a slim, working, full-stack website which can be (relatively) easily built, tested, and deployed on Google App Engine using GitHub actions. This README assume that the reader already has a basic familiarity with a broad range of topics and technologies, so it lacks explanation.

## Background

When I was 12 years old, sometime back in 1999, I developed a taste for, well, developing. Internet was dial-up with speeds up to 28 kbps (in a good day), I barely knew how to read in English, there was no google and I had a 50-minute-maximum-computer-daily-usage-policy, arbitrary set by Mrs. Mom. And that's when I decided to build my first HTML webpage. 

I used [geocities](https://web.archive.org/web/19990208004447/http://geocities.com/) free page builder to host my site, and was clever enough to tweak their standard code with windows notepad. I got it to look really pretty, despite the lack of resources, using frames with animated gifs and horizontal navbar. Check it out: [Woeclipse](https://web.archive.org/web/20090729143702/http://geocities.com/woeclipse/). Unfortunately, only the main page was archived. 

The site was a clan for playing Worms 2, a game developed by Team17. I joined a friend, Ricardo Werneck, and we both dedicate ourselves to make it work. Soon, the website was showing up in Brazil's most popular search engines (which we had to create the result entry ourselves), and we got people visiting our site daily. We managed to create a form through a 3rd party free service provider, which would send the data to my e-mail, and we got hundreds of applications. And then I figure out I didn't know what to do with the data we had.

How would the users create a secret password? How would they login? My website only had HTML files, and I had no clue on how to store and display data dynamically. I decided I need to join a website course. Mrs. Mom had other priorities, so I got stuck and never advanced the idea. 

Therefore, I owned myself this project. I know it is 22 years too late, and Worms 2 is not even supported on windows 64-bit architeture. So, I'm using Worms Armageddon instead, which had been just released in 1999. I hadn't played this for more than 2 decades, but I bought it to refresh my memory. If you are up to a match, I'm game! 

Also, I still have the contact of my childhood friend, and I will soon let him know that this was finally built. I think I owned him this, too.

That's the background. I have no idea if this will ever be useful, but I did learn a lot by developing it. 
I hope you find it amusing. Enjoy!

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

- All done! You can access the flask app in your browser either on `http://127.0.0.1:8000/` or `http://localhost:8000`.

### Populate the database

- You probably would like to create some users and events to check out some of this project's features, wouldn't you?
- Also, working with databases can be a little annoying. It would be awesome if there was an admin panel built-in, amirite?
- Well, say no more! I shipped this project with some JSON files that will do the trick. Once the flask app is running, access the following link:

    > [http://127.0.0.1:8000/populate_database](http://127.0.0.1:8000/populate_database)

- This will create a few users and events, and it should only work during development. 

### Admin Panel

- If you followed the last step correctly, you probably have one (and only one) admin user in your database: "zymmac". Weird nickname? The 12-year old me thought this very thoroughly to come up with, and it became my very own first e-mail username at [cheesemail.zzn.com](https://web.archive.org/web/20000302184741/http://cheesemail.zzn.com/email/portuguese/login/login.asp). Enough digression, so here's what you will do:
- Login using the credentials "zymmac" and password "123".
- You will notice a link in the right-side dropdown button, called "Admin Panel". 
- From there, you will be able to create, edit or delete events, add or remove users from events, and edit users admin permissions. 
- Make this secure: sign up your own user, log out, login with the admin user and set yourself as admin. Then, login with your credentials and remove zymmac from admin. Done! Only your password will be able to access the admin panel. 
- If something goes wrong, you can always follow the previous step, which resets all data back to the initial state, and try this step again.