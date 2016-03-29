from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from models import *
#~ from forms import *


class PantallaListView(ListView):
    model = Pantalla
    template_name = "pantalla_list.html"
    
class PantallaCreateView(CreateView):
    model = Pantalla
    template_name = "pantalla_new.html"    
    def get_success_url(self):
        return reverse_lazy("pantalla_list")

class PantallaDetailView(DetailView):
    model = Pantalla
    template_name = "pantalla_detail.html"
