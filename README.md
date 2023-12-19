# Paw-sibilities Rescue 🐾

## Description

Paw-sibilities Rescue is a heartwarming web application designed for a local animal rescue, fostering meaningful connections between rescue pets and compassionate volunteers. Our interactive platform serves as a hub for scheduling volunteer events, discovering adorable adoptable pets, and creating a paw-sitive impact in the lives of these lovable animals. Join us in making a difference, one paw at a time!

## Prerequisites

This application combines a React frontend with a Flask-SQLAlchemy backend. Before you begin, ensure you have the following installed on your local machine:

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)

If you would like to test email functionality, you will also need to sign up for a [Mailtrap](https://mailtrap.io/) (or other email server) account.
- Feel free to follow the instructions on [my blog](https://medium.com/@ktannehill/youve-got-flask-mail-6f2c7b1bb1e8) as well!

## How to Install

1. Fork and clone this repository into your local environment. Open the directory into your chosen code editor, such as VS Code.
  - Open `Explorer` on the top left of the window, and a terminal window - we will need to do a little setup before we get the app running.

2. App secret setup
  - In the main directory in `Explorer`, right click and create a new file named `.env`.
  - In your terminal window, run `pipenv install && pipenv shell` to install necessary dependencies and enter the Python virtual environment.
  - Run `flask shell` to enter the Flask shell, then run `import secrets; secrets.token_hex(32)` to generate a secret key. 
  - Copy the code; open the `.env` file and insert `APP_SECRET = <paste code here>`. Exit the shell with `Ctrl-D`

3. Flask-Mail configuration
  - This is where the blog post will come in handy! After you've signed up for Mailtral, navigate to `Email Testing > Inboxes > My Inbox > Show Credentials`.
  - Copy your username; in the `.env` file, insert `MAIL_USERNAME = <paste username here>`.
  - Copy your password; in the `.env` file, insert `MAIL_PASSWORD = <paste password here>`.
  - This should connect the app to your email server!

4. Backend:
  - Run `cd server` in the backend terminal window to navigate to the backend directory.
  - Run `flask db init`, `flask db migrate -m "initial migration"`, and `flask db upgrade` to create the database.
  - Run `python seed.py`. It may take a moment to seed the database!
    - Note: you may encounter an error in the terminal that usernames must be at least 5 characters long. Sometimes the seed file does not create long enough usernames! Run `python seed.py` again, it should populate the database appropriately. 
  - Run `flask run` or `python app.py` to start the server. Ensure it is running on port `5555`.
    - If for any reason it is not, run `FLASK_RUN_PORT = 5555`, then `flask run` again.

5. Frontend:
  - Open a second terminal window to be in charge of the frontend. Ensure you are in the main directory; if not, run `cd ..`.
  - Run `cd client` in the frontend terminal window to navigate to the frontend directory.
  - Run `npm i && npm start` to install necessary dependencies and start the application.

6. Enjoy using the application!

