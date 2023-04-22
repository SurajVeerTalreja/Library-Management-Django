from django.db import models

# Create your models here.
class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    user_text = models.TextField(max_length=200)


    def __str__(self) -> str:
        return f'{self.user_name}, Comment: {self.user_text}'



class Department(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self) -> str:
        return f'Department: {self.name}'


class PublicationDate(models.Model):
    date = models.DateField()

    def __str__(self) -> str:
        return f'Publication Date: {self.date}'
    

class Author(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'Author: {self.l_name}, {self.f_name}'


class Book(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.OneToOneField(PublicationDate, on_delete=models.SET_NULL, null=True)
    library_date = models.DateField(auto_now_add=True)
    department = models.ManyToManyField(Department)
    comments = models.ManyToManyField(Comment)
    slug = models.SlugField()
    is_bestselling = models.BooleanField()


    def __str__(self) -> str:
        return f'Book: {self.title}. Author: {self.author.l_name}'
