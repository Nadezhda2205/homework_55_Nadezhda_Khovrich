from django.db import models

class Task(models.Model):
    description = models.TextField(verbose_name='Задание', max_length=200, null=False, blank=False)
    status = models.CharField(
        verbose_name='Статус', 
        max_length=15, 
        null=False, 
        blank=False, 
        default='New')
    deadline = models.DateField(verbose_name='Дата выполнения', default=None)


    def __str__(self):
        return f"{self.description}"
        