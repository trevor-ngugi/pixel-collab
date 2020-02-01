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

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

class ImageTestClass(TestCase):
    def setUp(self):
        self.nairobi=Place(location='nairobi')
        self.nairobi.save()

        self.food=Category(name='food')
        self.food.save()

        self.post=Image(image='imagepic',image_name='food pic',description='nice food',location=self.nairobi,category=self.food)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))


    def test_save_method(self):
        self.post.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.post.delete_image()
        images=Image.objects.all()
        self.assertTrue(len(images)==0)

