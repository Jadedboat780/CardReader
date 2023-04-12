from django.db import models


class DjandoRegistration(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=200)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        managed = False
        db_table = 'djando_registration'
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"