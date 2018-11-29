from django.test import TestCase
from .models import Product

# Create your tests here.
class ProducTest(TestCase):
    """
    Here we'll define the tests that we'll run against out Product models
    """
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
