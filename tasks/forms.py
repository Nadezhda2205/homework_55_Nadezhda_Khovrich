from django import forms
from tasks.services.config import CHOICES
from datetime import date

class TaskForm(forms.Form):
    header = forms.CharField(max_length=200, required=True, label='Задание')
    description = forms.CharField(max_length=2000, required=True, label='Описание')
    status = forms.ChoiceField(choices=CHOICES, required=True, label='Статус')
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        initial=date.today(),
        label='Дата выполнения'
        )
