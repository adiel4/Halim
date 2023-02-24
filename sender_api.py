from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/a.ibraev/Downloads/credentials.json'
def gmail_send_message():
    creds, _ = google.auth.default(
    )

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content('This is automated draft mail')

        message['To'] = 'halimjonraimjanov@gmail.com'
        message['From'] = 'adiletibraev98@gmail.com'
        message['Subject'] = 'test message'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


if __name__ == '__main__':
    gmail_send_message()

import quickstart

a = quickstart.main()