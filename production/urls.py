from django.urls import path

from production import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('create/', views.CustomerCreate.as_view(), name='customer_create'),
    # path('', views.DocumentsJournalList.as_view(), name='documents_journal'),
]
