from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views


urlpatterns = [
    path('', views.restaurant_menu, name='restaurant_menu'),
    path('total', views.total, name='total'),
    path("get-dishes", views.GetAllDishes.as_view()),
    path("create-dish", views.CreateDishView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
