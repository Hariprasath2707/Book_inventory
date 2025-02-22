from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
