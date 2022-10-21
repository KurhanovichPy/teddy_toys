from django.db import models


class Goods(models.Model):
    id_good = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to='gallery', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Review(models.Model):
    user = models.CharField(max_length=20)
    body = models.TextField()
    mark = models.CharField(max_length=10)
    date = models.DateTimeField(format("%d %b %Y"))
