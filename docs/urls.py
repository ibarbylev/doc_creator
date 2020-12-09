from django.urls import path

from docs import views

urlpatterns = [
    path('', views.DocsListIndex.as_view(), name='index'),
    path('docs/<int:pk>/', views.DocsDetailsIndex.as_view(), name='doc_details'),
]
