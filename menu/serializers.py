from rest_framework import serializers
from .models import Dish, Allergen


class AllergenSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['title']


class DishSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True, queryset=Allergen.objects.all())

    class Meta:
        model = Dish
        fields = ['title', 'price', 'nutritional_value', 'allergens', 'picture', 'category']
