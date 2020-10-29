from django import forms
from django.forms import fields
from .models import Prestamista

class PrestamistaForm(forms.ModelForm):

    class Meta:
        model = Prestamista
        fields = [ "name", "last_name","address","phone"]
        updating= True


