from django.contrib import admin

from .models import Dish, Allergen

admin.site.register(Dish)
admin.site.register(Allergen)
