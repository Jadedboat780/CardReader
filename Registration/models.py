from django.db import models


class Registration(models.Model):
    username = models.CharField(max_length=150, blank=True, null=True)
    login = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'registration'
        verbose_name = 'преподавателя'
        verbose_name_plural = 'Зарегестрированные преподаватели'

    def __str__(self):
        return f'{self.username}'
