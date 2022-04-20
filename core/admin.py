from django.contrib import admin
from core import models
from . models import Clients, Client_certificate

admin.site.register(Clients)
admin.site.register(Client_certificate)

