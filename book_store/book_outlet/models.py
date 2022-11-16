from django.db import models

# Create your models here.

# class Book which inherits from class Model (build in class provided by Django)
class Book(models.Model):
    # attribute for title is indicator which data we want to store for attribute, charField = small to large strings
    #check Fieldtypes in documentation
    title = models.CharField(max_length=50) # required argument max_lenght
    rating = models.IntegerField() # no required argument
    
