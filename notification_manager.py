import smtplib
#written by ram 
from twilio.rest import Client

TWILIO_SID = "your SID"
TWILIO_AUTH_TOKEN = "Your auth Token"
TWILIO_VIRTUAL_NUMBER = ''
TWILIO_VERIFIED_NUMBER = ""
MY_EMAIL = "walternotsowhite69@gmail.com"
MY_PASSWORD = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.to_address = "tonystark2442005@gmail.com"

    def send_sms(self, message):
        print("SMS send")
        message = self.client.messages.create(
            body="Love you Mohit M \n\n    -Ishwariya -AML SONA ",
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)

            subject = "Low Price Alert!"
            # email_body = f"Subject:{subject}\n\n{email}"
            email_body = f"Love you Mohit M \n\n    -Ishwariya -AML SONA "
            # Encode the email body as UTF-8
            email_body = email_body.encode("utf-8")

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=self.to_address,
                msg=email_body,
            )

