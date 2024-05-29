import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.message import EmailMessage
from app.config import EMAIL_SENDER, EMAIL_SMTP, EMAIL_PORT, EMAIL_USER, EMAIL_PASS
from flask import render_template


def send_confirmacion():
    
    email_receiver = 'dcaceda@globalredsalud.com'

    email_subject = "Emisión de comprobantes"
    data = "prueba"
    email_body = render_template('step-01-solicitud.html', data=data)

    send_email_as(
        email_body,
        email_subject,
        email_receiver
    )

def send_email_siniestro(body, subject, email_receiver, blind_copy=""):
    email_sender = f"Comprobantes <{EMAIL_SENDER}>"
    # 1. Create an email message object
    message = EmailMessage()

    # 2. Configure email headers
    message["Subject"] = subject
    message["From"] = email_sender
    message["To"] = email_receiver
    if blind_copy:
        message["Bcc"] = blind_copy

    # 3. Set content
    message.set_content(body, subtype="html")

    try:

        # 3. Set SMTP server and PORT
        server = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
        # 4. Identify this client to the SMTP server
        server.ehlo()
        # 5. Secure the SMTP connection
        server.starttls()
        # 6. Login to email account
        server.login(EMAIL_USER, EMAIL_PASS)
        # 7. Send email
        server.send_message(message)
        # 8. Close connection to server
        server.quit()
        return True
    except Exception as err:
        print(err)
        return False

def send_email_as(body, subject, email_receiver, blind_copy=""):
    email_sender = f"Asistencias <{EMAIL_SENDER}>"
    # 1. Create an email message object
    message = EmailMessage()

    # 2. Configure email headers
    message["Subject"] = subject
    message["From"] = email_sender
    message["To"] = email_receiver
    if blind_copy:
        message["Bcc"] = blind_copy

    # 3. Set content
    message.set_content(body, subtype="html")

    try:

        # 3. Set SMTP server and PORT
        server = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
        # 4. Identify this client to the SMTP server
        server.ehlo()
        # 5. Secure the SMTP connection
        server.starttls()
        # 6. Login to email account
        server.login(EMAIL_USER, EMAIL_PASS)
        # 7. Send email
        server.send_message(message)
        # 8. Close connection to server
        server.quit()
        return True
    except Exception as err:
        print(err)
        return False

def send_email(body, subject, email_receiver, blind_copy=""):
    email_sender = f"Red Salud <{EMAIL_SENDER}>"
    # 1. Create an email message object
    message = EmailMessage()

    # 2. Configure email headers
    message["Subject"] = subject
    message["From"] = email_sender
    message["To"] = email_receiver
    if blind_copy:
        message["Bcc"] = blind_copy

    # 3. Set content
    message.set_content(body, subtype="html")

    try:
        # 3. Set SMTP server and PORT
        server = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
        # 4. Identify this client to the SMTP server
        server.ehlo()
        # 5. Secure the SMTP connection
        server.starttls()
        # 6. Login to email account
        server.login(EMAIL_USER, EMAIL_PASS)
        # 7. Send email
        server.send_message(message)
        # 8. Close connection to server
        server.quit()
        return True
    except Exception as err:
        print(err)
        return False


def send_email_with_files(body, subject, email_receiver, files=None, blind_copy=""):
    email_sender = f"Red Salud <{EMAIL_SENDER}>"
    # 1. Create an email message object
    message = MIMEMultipart()

    # 2. Configure email headers
    message["Subject"] = subject
    message["From"] = email_sender
    message["To"] = email_receiver
    if blind_copy:
        message["Bcc"] = blind_copy
    
    # 3. Set content
    message.attach(MIMEText(body, "html"))
    attach_files(message, files)

    try:
        # 3. Set SMTP server and PORT
        server = smtplib.SMTP(EMAIL_SMTP, EMAIL_PORT)
        # 4. Identify this client to the SMTP server
        server.ehlo()
        # 5. Secure the SMTP connection
        server.starttls()
        # 6. Login to email account
        server.login(EMAIL_USER, EMAIL_PASS)
        # 7. Send email
        server.send_message(message)
        # 8. Close connection to server
        server.quit()
        return True
    except Exception as err:
        print(err)
        return False


def attach_files(message, files):
    try:
        if not files:
            return False

        for file_pdf in files:
            if file_pdf.endswith(".pdf"):
                with open(file_pdf, "rb") as fil:
                    part = MIMEApplication(fil.read(), Name=file_pdf)
                part.add_header("Content-Disposition", "attachment", filename=file_pdf)
                message.attach(part)
        return True
    except Exception as e:
        print(e)
        return False
