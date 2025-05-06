from django.db import models
from django.utils import timezone

#criar uma entidade
class Category(models.Model):
    #cria um atributo
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

#criar uma entidade
class Contact(models.Model):
    #cria um atributo
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%M/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
