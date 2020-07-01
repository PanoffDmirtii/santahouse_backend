from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    coast = models.PositiveSmallIntegerField()
    cover = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.name}'
