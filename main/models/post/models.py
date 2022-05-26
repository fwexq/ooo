from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.CharField(max_length=80, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    status = models.CharField(max_length=40, verbose_name='Статус')
    published = models.BooleanField(default=True, verbose_name="Публикация")
    photo = models.ImageField(upload_to='media/post/images', verbose_name="Фото")

    class Meta:
        db_table = 'posts'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


