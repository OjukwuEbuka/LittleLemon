from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title="IceCream", Price=80.04, Inventory=100)
        self.item2 = Menu.objects.create(Title="CupCake", Price=40.06, Inventory=10)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(self.item1.__str__(), items[0].__str__())
        # self.assertEqual(self.item2.__str__(), items[1].__str__())