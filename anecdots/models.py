from django.db import models
from django.urls import reverse

class Anecdot(models.Model):
    text = models.TextField(verbose_name="Анекдот")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    change_date = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

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



class Authors(models.Model):
    author_name = models.CharField(max_length=100)
    def __str__(self):
        return self.author_name