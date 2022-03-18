from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Item

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'shopping_list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('items')


class RegisterUser(FormView):
    template_name = 'shopping_list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        return super(RegisterUser, self).get(*args, **kwargs)


class ItemList(LoginRequiredMixin, ListView):
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        context['count'] = context['items'].filter(complete=False).count()

        return context


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['product', 'quantity', 'unit', 'category', 'note']
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ItemCreate, self).form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['product', 'quantity', 'unit', 'category', 'note']
    success_url = reverse_lazy('items')


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('items')


class ItemComplete(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['complete']
    success_url = reverse_lazy('items')
    template_name = 'shopping_list/item_complete.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['form'])

        return context

    # def get(self, request, *args, **kwargs):
        # queryset = Item.complete
        # print(queryset)
        # Item.complete = True
        # print('request', request)
        # return self.post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.instance.complete = True
    #     return super(ItemComplete, self).form_valid(form)
