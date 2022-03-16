from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Item

# Create your views here.


class ItemList(ListView):
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['items'].filter(complete=False).count()

        return context


class ItemCreate(CreateView):
    model = Item
    fields = ['user', 'product', 'quantity', 'unit', 'category', 'note']
    success_url = reverse_lazy('items')
