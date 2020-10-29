from main.forms import PrestamistaForm
from django.shortcuts import get_object_or_404, redirect,render
from django.views import generic
# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from .models import Prestamista
from .forms import PrestamistaForm

class Prestamistas(generic.ListView):
    template_name ='main/index_prestamistas.html'
    context_object_name='all_prestamistas_list'
    
    def get_queryset(self):
        return Prestamista.objects.all()



class PrestamistaEdit(UpdateView):
    model = Prestamista
    fields =['name','last_name','address','phone','birthdate']
    template_name = 'edit_prestamista'

    def editing(request, ci):
        prestamista = get_object_or_404(Prestamista, ci=ci)
        if request.method == "POST":
            form = PrestamistaForm(request.POST, instance=prestamista)
            if form.is_valid():
                prestamista = form.save(commit=False)
                prestamista.save()
                return HttpResponseRedirect(reverse(viewname='main:prestamistas'))
        else:
            form = PrestamistaForm(instance=prestamista)
        return render(request, 'main/edit_prestamista.html', {'form': form})