from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# class Book which inherits from class Model (build in class provided by Django)
class Book(models.Model):
    # attribute for title is indicator which data we want to store for attribute, charField = small to large strings
    #check Fieldtypes in documentation
    title = models.CharField(max_length=50) # required argument max_lenght
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # no required argument
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
