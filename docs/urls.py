from django.urls import path

from docs import views

urlpatterns = [
    path('', views.index, name='index'),
]