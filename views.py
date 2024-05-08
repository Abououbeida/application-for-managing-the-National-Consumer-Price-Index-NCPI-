# Create your views here.
# ansade_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import FamilleProduit, Produit
from django.urls import reverse_lazy

# ansade_app/views.py



def home(request):
    return render(request, 'home.html')


def familleproduit_list(request):
    familles = FamilleProduit.objects.all()
    return render(request, 'familleproduit_list.html', {'familles': familles})

class FamilleProduitDetail(DetailView):
    model = FamilleProduit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produits'] = Produit.objects.filter(famille=self.object)
        return context

class FamilleProduitCreate(CreateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('familleproduit_list')

class FamilleProduitDelete(DeleteView):
    model = FamilleProduit
    success_url = reverse_lazy('familleproduit_list')

class FamilleProduitUpdate(UpdateView):
    model = FamilleProduit
    fields = '__all__'
    success_url = reverse_lazy('familleproduit_list')

class ProduitList(ListView):
    model = Produit

class ProduitDetail(DetailView):
    model = Produit

class ProduitCreate(CreateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')

class ProduitDelete(DeleteView):
    model = Produit
    success_url = reverse_lazy('produit_list')

class ProduitUpdate(UpdateView):
    model = Produit
    fields = '__all__'
    success_url = reverse_lazy('produit_list')
