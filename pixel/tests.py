from django.test import TestCase
from .models import  Place,Category,Image

# Create your tests here.

class PlaceTestClass(TestCase):
    def setUp(self):
        self.nairobi=Place(location='nairobi')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Place))
