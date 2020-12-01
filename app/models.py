from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def get_all_images_by_category_id(category_id):
        if category_id:
            return Image.objects.filter(category=category_id)
        else:
            return Image.objects.all()
        