from django.test import TestCase
from .models import  Place,Category,Image

# Create your tests here.

class PlaceTestClass(TestCase):
    def setUp(self):
        self.nairobi=Place(location='nairobi')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Place))

    def test_save_method(self):
        self.nairobi.save_place()
        locations=Place.objects.all()
        self.assertTrue(len(locations)>0)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.food=Category(name='food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

    def test_save_method(self):
        self.food.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)>0)

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

    def test_update_image(self):
        self.post.image='newimagepic'
        self.post.save()
        self.assertEqual(self.post.image,'newimagepic')

    def test_get_image_by_id(self):
        image=Image.get_image_by_id(self.post.id)
        self.assertEqual(image,self.post)



    

