from django.contrib import admin

from . models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    # to filter books by author and rating
    list_filter = ("author","rating")
    # display for admin in the grid to show title and author
    list_display = ("title", "author")

# Book model should be added to administrator site
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
