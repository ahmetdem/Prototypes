from email.message import EmailMessage
import ssl, smtplib

def SEND_EMAIL(receiver: str, password = "uwhiwfkfssbgdges"):
    """
    Sends an email with the values provided.
    """

    sender = 'randommailaccc@gmail.com'
    subject = 'the new announcement.'
    body = """
    To Person <ahmetyusufdmr88@gmail.com>

    An announcement has been made.
    """

    em = EmailMessage()

    em['From'] = sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())

    print('Email sent successfully.')