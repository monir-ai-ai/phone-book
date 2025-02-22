from django.urls import path
from .views import insert_contact, update_contact, delete_contact, search_contact

urlpatterns = [
    path('insert/', insert_contact, name='insert_contact'),
    path('update/<int:pk>/', update_contact, name='update_contact'),
    path('delete/<int:pk>/', delete_contact, name='delete_contact'),
    path('search/', search_contact, name='search_contact'),
]
