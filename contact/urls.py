from django.urls import path
from contact import views

app_name = 'contact'#definir a chamada do app

urlpatterns = [
    path('', views.index, name='index'),#definir o caminho
    path('search/', views.search, name='search'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
]
