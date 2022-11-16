import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='1901044@smartinternz.com',
    to_emails='1901044@smartinternz.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)