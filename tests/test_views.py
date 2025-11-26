from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuSerializerTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=120, inventory=10)
        Menu.objects.create(title="Burger", price=80, inventory=20)

    def test_get_all_serialized(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        # Just check that serialized data has the correct number of items
        self.assertEqual(len(serializer.data), 2)
        # Optionally, check the first item's title
        self.assertEqual(serializer.data[0]['title'], "Pizza")
