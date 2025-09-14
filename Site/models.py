from django.db import models

# Create your models here.

class category(models.Model):
    chinese_name=models.CharField(max_length=200)
    english_name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/')
    chinese_description=models.TextField()
    english_description=models.TextField()

class gallery(models.Model):
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    chinese_title=models.CharField(max_length=200)
    english_title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/')
    url=models.URLField(blank=True)

class profile(models.Model):
    chinese_name=models.CharField(max_length=200)
    english_name=models.CharField(max_length=200)
    chinese_role=models.CharField(max_length=200)
    english_role=models.CharField(max_length=200)
    chinese_university=models.CharField(max_length=200)
    english_university=models.CharField(max_length=200)
    image=models.ImageField(upload_to='static/')
    chinese_description=models.TextField()
    english_description=models.TextField()
