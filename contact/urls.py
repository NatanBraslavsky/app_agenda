from django.urls import path
from contact import views

app_name = 'contact'#definir a chamada do app

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),#definir o caminho
]
