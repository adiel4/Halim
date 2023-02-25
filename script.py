from PIL import Image, ImageFont, ImageDraw


def jpeg_to_pdf(filename,fio):
    image = Image.open(filename)
    im_1 = image.convert('RGB')
    end_file ='end_cert_'+ fio + '.pdf'
    try:
        im_1.save(end_file)
        with open('logs.txt','w') as k:
            k.write('adilet krasavchik')
            k.close()
    except:
        with open('logs.txt','w') as k:
            k.write('adilet krasavchik')
            k.close()


    return end_file


def edit_jpeg(filename: str, fio: str, id: str):
    image = Image.open(filename)
    ed_image = ImageDraw.Draw(image)
    font1 = ImageFont.truetype('gnyrwn971.ttf', 60)
    ed_image.text((500, 400), fio, font=font1, fill=(0, 0, 0))  # Задать позицию и цвет шрифта RGB
    ed_image.text((100, 100), id, font=font1, fill=(0, 0, 0))  # Задать позицию и цвет шрифта RGB
    image.save('edited_cert.jpg')
    image.show()
    end_file = jpeg_to_pdf('edited_cert.jpg', fio)
    return end_file



