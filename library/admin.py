from django.contrib import admin
from .models import Author, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # Number of extra forms displayed

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)
