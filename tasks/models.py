from django.db import models
from tasks.services.config import CHOICES

class Task(models.Model):
    header = models.TextField(verbose_name='Задание', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=500, null=True, blank=True)
    status = models.CharField(
        verbose_name='Статус', 
        max_length=15, 
        null=False, 
        blank=False, 
        default='New',
        choices=CHOICES)
    deadline = models.DateField(verbose_name='Дата выполнения', default=None)


    def __str__(self):
        return f"{self.header}"
        