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
    - Note: you may encounter an error in the terminal `Username must be between 5-50 characters`. Sometimes the seed file does not create long enough usernames! Run `python seed.py` again, it should populate the database appropriately. 
  - Run `flask run` or `python app.py` to start the server. Ensure it is running on port `5555`.
    - If for any reason it is not, run `FLASK_RUN_PORT = 5555`, then `flask run` again.

5. Frontend:
  - Open a second terminal window to be in charge of the frontend. Ensure you are in the main directory; if not, run `cd ..`.
  - Run `cd client` in the frontend terminal window to navigate to the frontend directory.
  - Run `npm i && npm start` to install necessary dependencies and start the application.

6. Enjoy using the application!

## Using the App

![Screenshot (4)](https://github.com/ktannehill/pawsibilitiesRescue/assets/139499376/626d1992-68c9-414f-af3c-69fb9b1108a8)

- Explore `Volunteer` or `View Pets` pages to view volunteer events or adoptable pets.
- Utilize search, sort, and filter options for targeted results.
- Click `See Details` for in-depth information on a specific pet or event.
- Sign up for an account, and be sure to check your Mailtrap account for the confirmation email!
  - Open the email, and follow the link provided to confirm your account.
- Now you'll be able to register for volunteer events. You'll receive another confirmation email once signed up!
- Visit your `Profile` page to manage your events, edit, or delete your account.
- Experience admin capabilities by logging in with credentials `admin`, and `password`.
  - The admin's account won't be confirmed by default, be sure to click the button to resend the confirmation email on the profile page and follow the steps.
- Note the admin has buttons to create new events and pets on their profile. Try it out!
- There are also additional buttons on each individual pet's and event's page to edit and delete them.
- Resize the window at any point to see the responsiveness of the page!

## Future Features

- You may have noticed two buttons I have not mentioned - `Foster` on a pet's page, and `View Fosters` on the admin's profile page. In the future, a user will be able to click `Foster` which will send an email to admins, and mark the foster as pending. The admins can view pending fosters via the button on their profile, and approve or deny them.
- Password reset emails/ links will also be incorporated in the future.
- JWT will provide additional security to the application.
- Email blasts to users when new events or pets are added to increase visibility and interaction.
- If you have any suggestions for features you would like to see, please let me know!

## Why I Made This App

As someone deeply passionate about animals and armed with nearly a decade of experience in the veterinary industry, I embarked on the journey of combining my lifelong love for animals with my newfound proficiency in programming. Before venturing into the world of coding, my family had always been active contributors to the rescue community—volunteering, fostering, and adopting. This application is a culmination of my personal experiences, reflecting not only my dedication to creating a positive impact in the lives of rescue pets but also showcasing the skills and knowledge gained throughout my programming journey. It's a heartfelt endeavor to merge my professional background with my love for animals, creating a meaningful and impactful tool that resonates with the values I hold dear. This project is not just a showcase of technical skills but a testament to the profound connection between personal passion and the transformative power of technology.

## Reflection

The past fifteen weeks at Flatiron School have been a whirlwind – a transformative journey that has not only expanded my knowledge but also shaped me into a more confident and capable programmer. I couldn't have imagined how much I would learn prior to entering this program. From the early days of grappling with JavaScript basics to navigating the intricacies of React, Python, SQL, and Flask, this experience has been challenging, rewarding, frustrating, exhilarating.

I am immensely proud of the collective accomplishments of our class; a group of more supportive, good-humored, and brilliant individuals I could not hope for. Special gratitude goes to my teammates for their collaboration on various projects and to our instructor, a bottomless well of knowledge and an inspiring mentor.

As I stand at the cusp of this milestone, armed with a solid foundation in software engineering, I eagerly anticipate the challenges and triumphs that lie ahead. Each late-night coding session has instilled in me the confidence to face new obstacles head-on. With unwavering determination, I am ready to ascend to new heights as a Software Engineer.

Thank you for an incredible journey, though only the first step. We did it!
