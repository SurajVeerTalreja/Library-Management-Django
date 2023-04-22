from django.contrib import admin
from .models import Book, Author, Department, PublicationDate, Comment

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('title', 'author', 'publication_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Department)
admin.site.register(PublicationDate)
admin.site.register(Comment)