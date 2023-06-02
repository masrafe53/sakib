from django.db import models

# Create your models here.
class offer(models.Model):
    title = models.CharField(max_length=100)
    discriptions = models.TextField(max_length=500)
    image = models.ImageField(upload_to='img')
    link = models.URLField(max_length=200, verbose_name='Link')
    def __str__(self) -> str:
        return self.title




class AllOffer(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img')
    link = models.URLField(max_length=200, verbose_name='Link')
    def __str__(self) -> str:
        return self.title

class head(models.Model):
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200, verbose_name='Link')
    image = models.ImageField(upload_to='img2')
    def __str__(self) -> str:
        return self.title
    