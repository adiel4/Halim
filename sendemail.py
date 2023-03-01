import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
from email import encoders
import pickle
import os
import time
body = '''Hi Adik,
We need to move on and refine the script
I will sent a 2000 email
'''
SCOPES = [
        "https://www.googleapis.com/auth/gmail.send"
    ]
creds_filename = 'token.pickle'

if os.path.exists(creds_filename):
    with open(creds_filename, 'rb') as f:
        creds = pickle.load(f)
else:
    flow = InstalledAppFlow.from_client_secrets_file(
        'creds.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open(creds_filename, 'wb') as f:
        pickle.dump(creds, f)
# flow = InstalledAppFlow.from_client_secrets_file(
#             'credentials.json', SCOPES)
# creds = flow.run_local_server(port=0)

service = build('gmail', 'v1', credentials=creds)
for i in range(1,1900):
    message = MIMEMultipart()
    message['to'] = 'joyforkg2@gmail.com'
    message['subject'] = 'Доработка скрипта'
    message.attach(MIMEText(body, 'plain'))
    pdfname = 'document.pdf'
# open the file in bynary
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload = MIMEBase('application', 'pdf', Name=pdfname)
    payload.set_payload((binary_pdf).read())
# enconding the binary into base64
    encoders.encode_base64(payload)
# add header with pdf name
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
    try:
        time.sleep(1)
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {message} Message Id: {message["id"]}')
    except HTTPError as error:
        print(F'An error occurred: {error}')
        message = None
