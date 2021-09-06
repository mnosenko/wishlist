from django.db import models


class Product(models.Model):
    """
    Таблица "Товар"

    Название товара
    Ссылка
    Цена товара
    Дата и время создания записи
    Двтв и время обновления записи
    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
