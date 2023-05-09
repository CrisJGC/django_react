from django.contrib import admin
from .models import Task # importamos el modelo del Task

# Register your models here.
admin.site.register(Task)