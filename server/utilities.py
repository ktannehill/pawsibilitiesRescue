from flask_mail import Message
from config import mail, s

def send_confirmation_email(user):
    token = s.dumps(user.email, salt="email-confirm")
    msg = Message(subject="Confirm Email", recipients=[user.email])
    link = f"http://127.0.0.1:4000/login/{token}"
    msg.html = f"<h2>Welcome, {user.first_name}!</h2> <p>Follow <a href={link}>this link</a> to activate your account.</p>"
    msg.content_type = "text/html"
    mail.send(msg)
    