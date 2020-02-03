from django.db import models

# Create your models here.
class Place(models.Model):
    location=models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_place(self):
        self.save()


class Category(models.Model):
    name=models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name=models.CharField(max_length =30)
    description=models.TextField() 
    location=models.ForeignKey(Place )#add default to 0
    category=models.ForeignKey(Category)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image(cls,id):
        return cls.objects.filter(id=id).delete()

    @classmethod
    def get_image_by_id(cls,id):
        return cls.objects.filter(id=id)[0]

    @classmethod
    def show_images(cls):
        return cls.objects.order_by('image_name')

    @classmethod
    def search_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images


    #write update method




    # class Meta:                                            for ordering
    #     ordering = ['first_name']


