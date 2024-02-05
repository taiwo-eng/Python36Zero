import smtplib as mailer
import ssl


def send_email(message, receiver):
    host = "smtp.gmail.com"
    port = 465

    contact_page_app_username = "taiwoakinnusoye@gmail.com"
    contact_page_app_password = "oyse elbx tmuw afli"

    context = ssl.create_default_context()

    with mailer.SMTP_SSL(host, port, context=context) as server:
        server.login(contact_page_app_username, contact_page_app_password)
        server.sendmail(contact_page_app_username, receiver, message)
