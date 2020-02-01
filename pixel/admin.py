from django.contrib import admin
from .models import Place,Image,Category

# Register your models here.
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Image)