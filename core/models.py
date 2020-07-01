from django.db import models


class Base(models.Model):
    name = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    cover = models.ImageField(upload_to='media/')
    weight = models.PositiveSmallIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Product(Base):
    coast = models.PositiveSmallIntegerField('Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class PopularProduct(Base):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, name='Товар')

    class Meta:
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'


class Stock(Base):
    dtm_start = models.DateTimeField('Начало акции')
    dtm_end = models.DateTimeField('Конец акции')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
