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
    ed_image.text((500, 400), fio, font=font1, fill=(0, 0, 0))  # Задать позицию и цвет шрифта RGB
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

from base64 import urlsafe_b64encode

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
            flow = InstalledAppFlow.from_client_secrets_file('/home/adilet/Downloads/adilet.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)


service = gmail_auth()


def add_att(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read().decode(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)


def build_msg(dest, obj, body, att=[]):
    if not att:
        message = MIMEText(body)
        message['to'] = dest
        message['from'] = email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = dest
        message['from'] = email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for file in att:
            add_att(message, file)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


def send_msg(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
        userId='me',
        body=build_msg(destination, obj, body, attachments)
    )


send_msg(service, 'joyforkg3@gmail.com', 'test msg', 'congrats you get cert', [])
