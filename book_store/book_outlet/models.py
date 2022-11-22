from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# class Book which inherits from class Model (build in class provided by Django)
class Book(models.Model):
    # attribute for title is indicator which data we want to store for attribute, charField = small to large strings
    #check Fieldtypes in documentation
    title = models.CharField(max_length=50) # required argument max_lenght
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # no required argument
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default = False)
                                                    # turning attribute as index so the search is faster
    slug = models.SlugField(default="",blank=True, null=False, db_index=True) #Harry Pooter 1 => harry-potter-1
                                        #blank=True <-- slug filed is not mandatory
                                        #editable = False <-- make field non editable

    # method to get url that should represent and load data for this specific model
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    #Overwritting save method
    def save(self, *args, **kwargs):
        # convert title to slug
        self.slug = slugify(self.title)

        #We have to make sure to call super save method so that Django build save method is still getting called
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} ({self.rating})"
