from django.shortcuts import render
from django.views.generic import FormView, ListView  # Corrected import
from django.urls import reverse_lazy
from .forms import ProductForm
from .models import Product

# Create your views here.
class ProductFormView(FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('list_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(ListView):
    model = Product
    template_name = "products/list_product.html"
    context_object_name = 'products'
