#encoding:utf-8
from django.db import models
#from django.contrib.auth.models import User
#from recognition.models import Recognition
from vulnerability.models import Vulnerability
 
class Report(models.Model):
    client = models.ForeignKey('Client')
    name = models.ForeignKey('Title_report')
    customer_logo = models.ImageField(upload_to = 'logo_client')
    type_pentest = models.ForeignKey('Type_pentest')
#    date = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    introduction = models.TextField()
    objetive = models.TextField()
#    recognition = models.ForeignKey('Recognition')
    vulnerability = models.ForeignKey('Vulnerability')
    affected_elements = models.ForeignKey('Affected_elements')
    evidences = models.ForeignKey('Evidences_images')

    def __str__(self):
        return self.client
 
class Client(models.Model):
    name_client = models.CharField(max_length=30)

    def __str__(self):
        return self.name_client

class Title_report(models.Model):
    report_name = models.CharField(max_length=30)

    def __str__(self):
        return self.report_name
 
 
class Type_pentest(models.Model):
    type_pent = models.CharField(max_length=30)
    
    def __str__(self):
        return self.type_pent
 
class Affected_elements(models.Model):
    elements = models.TextField()
    
    def __str__(self):
        return self.elements

class Evidences_images(models.Model):
    images_e = models.ImageField(upload_to = 'images_evidences')
    
    def __str__(self):
        return self.images_e
