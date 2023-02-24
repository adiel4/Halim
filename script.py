from PIL import Image, ImageFont, ImageDraw


def jpeg_to_pdf(filename):
    image = Image.open(filename)
    im_1 = image.convert('RGB')
    try:
        im_1.save('end_cert.pdf')
        with open('logs.txt','w') as k:
            k.write('adilet krasavchik')
            k.close()
    except:
        with open('logs.txt','w') as k:
            k.write('adilet krasavchik')
            k.close()


    return True


def edit_jpeg(filename: str, fio: str, id: str):
    image = Image.open(filename)
    ed_image = ImageDraw.Draw(image)
    font1 = ImageFont.truetype('gnyrwn971.ttf', 60)
    ed_image.text((500, 400), fio, font=font1, fill=(0, 0, 0))  # Задать позицию и цвет шрифта RGB
    ed_image.text((100, 100), id, font=font1, fill=(0, 0, 0))  # Задать позицию и цвет шрифта RGB
    image.save('edited_cert.jpg')
    jpeg_to_pdf('edited_cert.jpg')
    return True

edit_jpeg('raw_cert.jpg','','13413515')


