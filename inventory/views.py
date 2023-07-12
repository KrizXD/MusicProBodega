from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Stock
from .forms import StockForm
from django_filters.views import FilterView
from .filters import StockFilter
from rest_framework import generics
from .serializers import StockSerializer
from faker import Faker

fake = Faker()

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10


class StockCreateView(SuccessMessageMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = "edit_stock.html"
    success_url = '/inventory'
    success_message = "Stock se ha creado correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Stock'
        context["savebtn"] = 'Agregar al Inventario'
        return context

    def form_valid(self, form):
        num_products = 1000  # Número de productos a generar
        for _ in range(num_products):
            product = Stock()
            product.generate_fake_data()  # Generar datos ficticios
            product.save()
        return super().form_valid(form)


class StockUpdateView(SuccessMessageMixin, UpdateView):
    model = Stock
    form_class = StockForm
    template_name = "edit_stock.html"
    success_url = '/inventory'
    success_message = "Stock se ha actualizado correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Stock'
        context["savebtn"] = 'Actualizar Stock'
        context["delbtn"] = 'Eliminar Stock'
        return context


class StockDeleteView(View):
    template_name = "delete_stock.html"
    success_message = "Stock se ha borrado correctamente"

    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        stock.delete()
        messages.success(request, self.success_message)
        return redirect('inventory')


class StockList(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def recibir_formulario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productos_solicitados = data['productos']
        respuesta = {'disponibles': [], 'no_disponibles': []}
        for producto in productos_solicitados:
            try:
                stock_obj = Stock.objects.get(name=producto['nombre'])
                if stock_obj.quantity >= producto['cantidad']:
                    respuesta['disponibles'].append(producto)
                else:
                    respuesta['no_disponibles'].append(producto)
            except Stock.DoesNotExist:
                respuesta['no_disponibles'].append(producto)

        return JsonResponse(respuesta)
    else:
        return JsonResponse({'error': 'Método no permitido'})

