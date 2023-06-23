import smtplib
from email.mime.text import MIMEText
from user_fetcher import UserFetcher


class Mailer(object):

    def send(self, sender, recipient, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipient]
        s = smtplib.SMTP('localhost')
        s.send_message(recipient)
        s.quit()


# if __name__ == "__main__":
#     with open('users.csv', 'r') as csv_file:
#         reader = csv.DictReader(csv_file)
#         users = [row for row in reader]
#     mailer = Mailer()
#     mailer.send(
#         'me@example.com',
#         [x["email"] for x in users],
#         "This is your message", "Have a good day"
#     )

# here goes the new version of the logi with separated fetcher

if __name__ == '__main__':
    user_fetcher = UserFetcher('users.csv')
    mailer = Mailer()
    mailer.send(
        'me@example.com',
        [x["email"] for x in user_fetcher.fetch_users()],
        "This is your message", "Have a good day"
    )

'''This design principle is called Separation of Concern (SoC), and sooner 
or later you will either be very thankful you adhered to it or very sorry 
that you did not. You have been warned. Let’s follow our own advice and 
separate the retrieval of user information from the EmailSender class. Se we
create the new file called  user_fetcher.py'''

'''Can you see how it might take a bit of effort to get this right, but how 
much easier it will be when we want to drop in Postgres, Redis, or some 
external API without changing the code that does the actual sending of the 
email?
 
 How could you create some sort of messaging interface that would allow you 
 to send messages to many different platforms without changing the code 
 doing the sending to fit each target, or reinventing the wheel to fit your 
 needs? The more general problem we want to solve is: The interface I have 
 is not the interface I want! '''
