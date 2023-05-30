from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from inventory.models import Stock
from transactions.models import SaleBill, PurchaseBill
from .api import obtener_saludo
from .api import obtener_productos

class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        labels = []
        data = []
        stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
        sales = SaleBill.objects.order_by('-time')[:3]
        purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels': labels,
            'data': data,
            'sales': sales,
            'purchases': purchases
        }
        return render(request, self.template_name, context)

def mi_vista(request):
    saludo = obtener_saludo()

    return render(request, 'saludo.html', {'saludo': saludo})

def mostrar_productos(request):
    productos = obtener_productos()
    return render(request, 'productos.html', {'productos': productos})

class AboutView(TemplateView):
    template_name = "about.html"
