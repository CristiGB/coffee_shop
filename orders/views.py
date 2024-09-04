from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from .models import Order, OrderProduct
from .forms import OrderProductForm

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['total'] = sum(product_order.total_price for product_order in order.orderproduct_set.all())
        return context


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    #template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('my-order')

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)

@require_POST
def update_order_product_quantity(request):
    product_id = request.POST.get('product_id')
    new_quantity = request.POST.get('quantity')
    
    try:
        order_product = OrderProduct.objects.get(id=product_id, order__user=request.user, order__is_active=True)
        order_product.quantity = int(new_quantity)
        order_product.save()
        
        order = order_product.order
        total = sum(product_order.total_price for product_order in order.orderproduct_set.all())
        
        response = {
            'success': True,
            'new_quantity': order_product.quantity,
            'total_price': order_product.total_price,
            'order_total': total
        }
    except OrderProduct.DoesNotExist:
        response = {'success': False, 'error': 'Order product not found.'}

    return JsonResponse(response)


class DeleteOrderProductView(LoginRequiredMixin, DeleteView):
    model = OrderProduct
    success_url = reverse_lazy('my-order')

    def get_object(self, queryset=None):
        return get_object_or_404(OrderProduct, id=self.kwargs['pk'], order__user=self.request.user, order__is_active=True)

    def form_valid(self, form):
        messages.success(self.request, 'Producto eliminado con éxito.')  # Mensaje de éxito
        return super().form_valid(form)
    