#encoding:utf-8
from django.db import models

class Recognition(models.Model):  
    subtitle = models.CharField(max_length=50)
    description = models.TextField()
    urls = models.ForeignKey('Urls')
    images_id = models.ForeignKey('Images_recognition')    

    def __str__(self):
        return self.subtitle

class Urls(models.Model):
    urls_i = models.URLField()

    def __str_(self):
        return self.urls

class Images_recognition(models.Model):
    images = models.ImageField(upload_to ='images_evidences')

    def __str__(self):
        return self.picture_path.name

