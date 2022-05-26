from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models.user.managers import UserManager


class User(AbstractUser):
    username = None
    last_login = None
    date_joined = None
    email = models.EmailField(max_length=40, unique=True, verbose_name='email aдрес',)
    first_name = models.CharField(max_length=40, verbose_name='Имя пользователя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия пользователя')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name='Аватар')
    api_key = models.CharField(max_length=60, verbose_name='API ключ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

