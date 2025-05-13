from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return f"Имя: {self.name}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    book_name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, default='Не указан')
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.book_name}, {self.price}"


