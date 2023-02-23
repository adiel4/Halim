import io
from PIL import Image, ImageFont, ImageDraw

def jpeg_to_pdf(filename):
    image = Image.open('edited_cert.jpg')
    im_1 = image.convert('RGB')
    im_1.save('end_cert.pdf')
    pass

def edit_jpeg(filename, fio, id):
    image = Image.open(filename)
    ed_image = ImageDraw.Draw(image)
    font1 = ImageFont.truetype('gnyrwn971.ttf', 60)
    ed_image.text((500, 400), fio, font=font1, fill=(0, 0, 0)) #Задать позицию и цвет шрифта RGB
    image.save('edited_cert.jpg')
    jpeg_to_pdf('edited_cert.jpg')
    return True


def send_mail(mail_to, text, file_pdf):
    pass


# print(edit_jpeg('raw_cert.jpg', 'adilet Ibraev', '0130314031'))

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from base64 import urlsafe_b64decode, urlsafe_b64encode

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

SCOPES = ['https://mail.google.com/']
email = 'adiletibraev98@gmail.com'

def gmail_auth():
    creds = None
    if os.path.exists('token.pickle'):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('C:\Users\a.ibraev\Downloads\adilet.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds,token)
    return build('gmail', 'v1', credentials=creds)

service = gmail_auth()
