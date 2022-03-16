from django.urls import path
from .views import ItemList, ItemCreate

urlpatterns = [
    path('', ItemList.as_view(), name='items'),
    path('item-create/', ItemCreate.as_view(), name='item-create')
]