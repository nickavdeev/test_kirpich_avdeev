from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Dish
from .serializers import DishSerializer


def restaurant_menu(request):
    dishes = {}
    for category in Dish.categories:
        dishes_by_category = []

        for dish in Dish.objects.values():
            if category[0] == dish['category']:
                allergens = []
                for allergen in Dish.objects.get(dish_id=dish['dish_id']).allergens.values():
                    allergens.append(allergen['title'])
                dish['allergens'] = 'нет' if len(allergens) == 0 else ', '.join(allergens)
                dish['picture'] = f'/{dish["picture"]}'

                dishes_by_category.append(dish)

        dishes.update({category[0]: dishes_by_category})

    return render(request, 'menu/index.html', {'dishes': dishes})


def total(request):
    total_sum = 0
    dishes = []
    allergens = []

    if request.method == 'POST':
        for dish_id in request.POST:
            if dish_id != 'csrfmiddlewaretoken':
                total_sum += Dish.objects.get(dish_id=int(dish_id)).price
                dishes.append(Dish.objects.get(dish_id=int(dish_id)).title)

                for allergen in Dish.objects.get(dish_id=int(dish_id)).allergens.values():
                    if allergens.count(allergen['title']) == 0:
                        allergens.append(allergen['title'])

    return render(request, 'menu/total.html', {'total_sum': total_sum, 'dishes': dishes, 'allergens': allergens})


class GetAllDishes(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class CreateDishView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
