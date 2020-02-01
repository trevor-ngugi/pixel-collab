from django.test import TestCase
from .models import  Place,Category,Image

# Create your tests here.

class PlaceTestClass(TestCase):
    def setUp(self):
        self.nairobi=Place(location='nairobi')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Place))

class CategoryTestClass(TestCase):
    def setUp(self):
        self.food=Category(name='food')
        self.assertTrue(isinstance(self.food,Category))

class ImageTestClass(TestCase):
    def setUp(self):
        self.post=Image(image='imagepic',image_name='food pic',description='nice food')
        self.assertTrue(isinstance(self.post,Image))
        
