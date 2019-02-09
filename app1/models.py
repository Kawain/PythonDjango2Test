from django.db import models
from django.urls import reverse


class Category(models.Model):
    """カテゴリ"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'category'


class Memo(models.Model):
    """内容"""

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="カテゴリ"
    )
    title = models.CharField("タイトル", max_length=255)
    detail = models.TextField("内容")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # データ保存処理後にリダイレクトするURL
        return reverse("app1:detail", kwargs={"pk": self.id})

    class Meta:
        managed = False
        db_table = 'memo'
