from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()


class Author(models.Model):
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    date_brith = models.DateField(auto_now=False)
    avatar = models.ImageField(upload_to='author/avatar/', verbose_name='Аватар')


class Books(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ManyToManyField('Author', related_name='books_author')
    book = models.FileField(upload_to='book/', verbose_name='Книга')
    image = models.ImageField(upload_to='book/image/', verbose_name='Обложка')
    title = models.CharField(max_length=128)
    desc = models.TextField()
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    def restore(self):
        self.is_active = True
        self.title = self.title[1:]
        self.save()
        return self
   