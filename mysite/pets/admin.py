from django.contrib import admin

from pets.models import Pet, Type

# Register your models here.

admin.site.register(Pet)
admin.site.register(Type)