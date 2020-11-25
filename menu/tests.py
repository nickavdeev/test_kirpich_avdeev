from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_jwt.serializers import User

from .models import Allergen


class TestMenu(APITestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(username="test")
        self.client.force_authenticate(user=user)
        self.allergen = Allergen.objects.create(title="1")

        self.dish = {
            'title': "Блюдо 2",
            'price': 1.0,
            'nutritional_value': 1,
            'allergens': [self.allergen.id],
            'category': 'Закуски',
        }

    def test_return_200(self):
        response = self.client.get("/api/v1/menu/get-dishes")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dish(self):
        response = self.client.post(
            "/api/v1/menu/create-dish", self.dish, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_dish_from_empty_title(self):
        self.dish['title'] = ''
        response = self.client.post(
            "/api/v1/menu/create-dish", self.dish, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_dish_from_incorrect_price(self):
        self.dish['price'] = -1.0
        response = self.client.post(
            "/api/v1/menu/create-dish", self.dish, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_dish_from_incorrect_nutritional_value(self):
        self.dish['nutritional_value'] = -1
        response = self.client.post(
            "/api/v1/menu/create-dish", self.dish, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
