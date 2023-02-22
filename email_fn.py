# https://developers.google.com/gmail/api/guides/sending
import base64

from email.mime.text import MIMEText

import discovery


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    return message

service = discovery.build('gmail', 'v1', credentials=creds)


def create_and_send_email(sender, receiver, subject, content, service):
    email_message = create_message(sender, receiver, subject, content)
    send_message(service, OVERALL_RECEIVER, email_message)


create_and_send_email(OVERALL_RECEIVER, OVERALL_RECEIVER, "German Immigration Automation", "Selenium Script has Begun", service)
print("Sent email confirming start of script.")