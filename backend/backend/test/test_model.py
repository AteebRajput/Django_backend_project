from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from littlelemonapi.models import Menu,MenuItem
from littlelemonapi.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(name='TestMenu1', price=10.99)
        Menu.objects.create(name='TestMenu2', price=15.99)
        Menu.objects.create(name='TestMenu3', price=8.99)

    def test_getall(self):
        # Retrieve all Menu objects added for the test purpose
        url = reverse('menu-list')  # Replace 'menu-list' with the actual URL name for your view
        response = self.client.get(url)

        # Serialize the retrieved objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert if the serialized data equals the response
        self.assertEqual(response.data, serializer.data)
        
class MenuItemTest(TestCase):
 def test_get_item(self):
    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    self.assertEqual(item, "IceCream : 80")

