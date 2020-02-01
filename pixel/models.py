from django.db import models

# Create your models here.
class Place(models.Model):
    location=models.CharField(max_length =30)

    def __str__(self):
        return self.location

class Category(models.Model):
    name=models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image=models.CharField(max_length =30)
    image_name=models.CharField(max_length =30)
    description=models.TextField() 
    location=models.ForeignKey(Place )#add default to 0
    category=models.ForeignKey(Category)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # class Meta:                                            for ordering
    #     ordering = ['first_name']


