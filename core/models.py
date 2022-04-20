from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Clients(models.Model):
    client_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=32)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.client_name


class Client_certificate(models.Model):
    certificate_name = models.CharField(max_length=200)
    logo = models.ImageField()
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.certificate_name

    def save(self, *args, **kwargs):
        x = 'mahin'
        qrcode_img = qrcode.make(self.certificate_name)
        canvas = Image.new('RGB', (350, 350), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.certificate_name} \n {self.description}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
        # info = " Name: {name} \n Passport No {passport} \n Trade: {trade} \n Training Center: {center}\n Website: {website} ".format(name = student.name, passport = '123B234', trade = "6G", center="JTC Training Center", website="https://jtcbd.net")
