from django.db import models


class FirstTable(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    esp = models.TextField(db_column='ESP')  # Field name made lowercase.
    id_card = models.IntegerField(db_column='ID_card')  # Field name made lowercase.
    group = models.CharField(db_column='Group', max_length=20, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=200)  # Field name made lowercase.
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'first_table'
        verbose_name = "Объект"
        verbose_name_plural = "Посещаемость"

    def __str__(self):
        return f'{self.group} {self.username} {self.time.time()}'

