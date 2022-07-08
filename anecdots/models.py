from django.db import models
from django.urls import reverse
from django.conf import settings


class Anecdot(models.Model):
    text = models.TextField(verbose_name="Анекдот")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    change_date = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Анекдот"
        verbose_name_plural = "Анекдоты"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('cats',kwargs={'category_id':self.pk})


class Comments(models.Model):
    anecdot = models.ForeignKey(Anecdot,on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    is_changed = models.BooleanField(default=False)
    change_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
# class Authors(models.Model):
#     author_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.author_name