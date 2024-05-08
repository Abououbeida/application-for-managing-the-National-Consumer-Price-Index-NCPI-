from django.contrib import admin

# Register your models here.
# ansade_app/admin.py

from .models import FamilleProduit, Produit

admin.site.register(FamilleProduit)
admin.site.register(Produit)

