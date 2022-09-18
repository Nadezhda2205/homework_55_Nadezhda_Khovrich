from django.contrib import admin
from django.urls import path
from tasks.views import index_view, add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('add/', add_view),
]

