from django.db import models


class CoupleInfo(models.Model):
    esp = models.TextField(blank=True, null=True)
    id_card = models.IntegerField(blank=True, null=True)
    student_group = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    in_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'coupleinfo'
        verbose_name = 'пару'
        verbose_name_plural = 'Информация о парах'

    def __str__(self):
        return f'{self.username} {self.id_card}'

