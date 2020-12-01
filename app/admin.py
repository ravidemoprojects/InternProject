from django.contrib import admin
from .models import Image, Category
# Register your models here.


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display =['id','photo','category']

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']