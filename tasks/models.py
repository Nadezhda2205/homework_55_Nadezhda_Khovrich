from django.db import models
from tasks.services.config import CHOICES
from django.utils import timezone

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
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)


    def __str__(self):
        return f"{self.header}"
        

    def delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

