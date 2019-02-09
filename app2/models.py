from django.db import models


class Category(models.Model):
    """カテゴリ"""

    name = models.CharField("カテゴリ名", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'
