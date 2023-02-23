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


print(edit_jpeg('raw_cert.jpg', 'adilet Ibraev', '0130314031'))
