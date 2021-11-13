import smtplib
from .email_credentials import email_address, email_password
from email.message import EmailMessage


def create_email(Subject, From, To, Content):
    msg = EmailMessage()
    msg["Subject"] = Subject
    msg["From"] = From
    msg["To"] = To
    msg.set_content(Content)
    return msg


def send_email(login_email, login_password, msg):
    """create your login_password at https://myaccount.google.com/apppasswords"""
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smpt:
        smpt.login(login_email, login_password)
        smpt.send_message(msg)


def main():
    msg = create_email("Test Subject", email_address,
                       email_address, "Test Body")
    send_email(email_address, email_password, msg)


if __name__ == "__main__":
    main()
