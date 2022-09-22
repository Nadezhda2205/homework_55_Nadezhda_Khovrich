from django.contrib import admin
from django.urls import path
from tasks.views import index_view, add_view, edit_view, delete_view, about_view, detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('add/', add_view, name='task_add'),
    path('edit/<int:pk>', edit_view, name='task_edit'),
    path('delete/<int:pk>', delete_view, name='task_delete'),
    path('about/', about_view, name='about'),
    path('detail/<int:pk>', detail_view, name='task_detail'),
]

