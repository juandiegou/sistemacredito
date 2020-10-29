from django.contrib import admin

from .models import Prestamista,Prestamos,Cuota

# Register your models here.

admin.site.register(Prestamista)
admin.site.register(Prestamos)
admin.site.register(Cuota)