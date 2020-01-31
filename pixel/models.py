from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.CharField(max_length =30)
    image_name=models.CharField(max_length =30)
    description=models.CharField(max_length =30)

    def __str__(self):
        return self.image_name

    # class Meta:                                            for ordering
    #     ordering = ['first_name']

class Location(models.Model):
    place=models.CharField(max_length =30)

    def __str__(self):
        return self.place

class Category(models.Model):
    name=models.CharField(max_length =30)

    def __str__(self):
        return self.name