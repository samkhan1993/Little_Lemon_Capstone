from django.test import TestCase
from littlelemon.restaurant.models import Menu
from littlelemon.restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item=Menu.objects.create(title="IceCream", price=80, Inventory=110)
        self.item2=Menu.objects.create(title="Burger", price=90, Inventory=120)

    def test_getall(self):
        menus=Menu.objects.all()
        serializer=MenuSerializer(menus, many=True)

        self.assertEqual(menus, 'IceCream : 80')
        self.assertEqual(menus, 'Burger : 90')