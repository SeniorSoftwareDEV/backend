from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime, jwt
import smtplib
from utils.email_html import html_template

SECRET_KEY = 'Tradin_Buddy'

def encode_auth_token(email):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600),
            'iat': datetime.datetime.utcnow(),
            'sub': email
        }
        
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e
      
def decode_auth_token(auth_token):
    """
    Validates the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms="HS256")
        return '200'
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def verifyEmail(email, firstName):
    try:
        print(type(email), firstName)
        msg = MIMEMultipart()
        msg["From"] = "comma0517@gmail.com"
        msg["To"] = email
        msg["Subject"] = "Verify your email address"
        token = encode_auth_token(email=email)
        # msg.attach(MIMEText(message))
        html_message = html_template.render(token=token, firstName=firstName)
        msg.attach(MIMEText(html_message, 'html'))

        mailserver = smtplib.SMTP("smtp.gmail.com", 587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login("comma0517@gmail.com", "lrdasrmtbpqovtti")

        mailserver.sendmail("comma0517@gmail.com", email, msg.as_string())

        mailserver.quit()
    except Exception as e:
        print(str(e))
        return 400
    return 200
