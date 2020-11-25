from django.core.validators import MinValueValidator
from django.db import models


class Allergen(models.Model):
    title = models.CharField('Название', max_length=100, default='')

    class Meta:
        verbose_name_plural = "Аллергены"
        verbose_name = "Аллерген"

    def __str__(self):
        return f'{self.title}'


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=100, default='')
    price = models.FloatField('Цена', default=0, help_text='В рублях',
                              validators=[MinValueValidator(0.0)])
    nutritional_value = models.IntegerField('Пищевая ценность', default=0, help_text='В ккал/г',
                                            validators=[MinValueValidator(0.0)])
    allergens = models.ManyToManyField(Allergen, default=None, related_name='allergens', blank=True)
    picture = models.ImageField('Картинка', upload_to='static/menu/img', default=None)

    snacks = 'Закуски'
    salads = 'Салаты'
    soups = 'Супы'
    meat = 'Мясо'
    pizza = 'Пицца'
    dessert = 'Десерты'
    categories = (
        (snacks, 'Закуски'),
        (salads, 'Салаты'),
        (soups, 'Супы'),
        (meat, 'Мясо'),
        (pizza, 'Пицца'),
        (dessert, 'Десерты'),
    )
    category = models.CharField('Категория', max_length=100, choices=categories, default=snacks)

    class Meta:
        verbose_name_plural = "Меню ресторана"
        verbose_name = "Блюдо"

    def __str__(self):
        return f'{self.title}'
