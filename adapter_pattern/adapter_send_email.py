import csv
import smtplib
from email.mime.text import MIMEText
from user_fetcher import UserFetcher


class Mailer:

    @staticmethod
    def send(sender, recipient, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        s = smtplib.SMTP('localhost', 8025)
        s.send_message(msg=msg)
        s.quit()


class Logger:
    @staticmethod
    def output(self, message):
        print(f'[Logger: {message}]')


class LoggerAdapter(object):
    def __init__(self, what_i_have):
        self.what_i_have = what_i_have

    def send(self, sender, recipients, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(
            sender,
            recipients,
            subject,
            message
        )
        self.what_i_have.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_have, attr)


if __name__ == "__main__":
    user_fetcher = UserFetcher('users.csv')
    mailer = Mailer()
    for recipient in [x["email"] for x in user_fetcher.fetch_users()]:
        mailer.send(
            'me@example.com',
            recipient,
            'This is your message',
            'Have a good day'
        )
