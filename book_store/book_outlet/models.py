from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    # Class nested in Address class (to add metaconfiguration of our model, to configure behaviours of our model, to register special settings which will affect how the model is used (In our case Address))
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # ONE to ONE assotation
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null = True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

# class Book which inherits from class Model (build in class provided by Django)
class Book(models.Model):
    # attribute for title is indicator which data we want to store for attribute, charField = small to large strings
    #check Fieldtypes in documentation
    title = models.CharField(max_length=50) # required argument max_lenght
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # no required argument
    # pointer to the Author as other class which is conected to Book (One to Many)
    # on_delete says if Author is deleted all releted Books should be deleted
    # related name is name on which we query to retrieve the related model
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default = False)
                                                    # turning attribute as index so the search is faster
    slug = models.SlugField(default="",blank=True, null=False, db_index=True) #Harry Pooter 1 => harry-potter-1
                                        #blank=True <-- slug filed is not mandatory
                                        #editable = False <-- make field non editable

    # MANY to MANY assotiation, Many to many creates additional mapping table and there is no need for on_delete
    published_countries = models.ManyToManyField(Country)

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
