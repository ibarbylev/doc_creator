from django.urls import path

from production import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('create/', views.CustomerCreate.as_view(), name='customer_create'),
    path('update/<int:pk>/', views.CustomerUpdate.as_view(), name='customer_update'),
    path('delete/<int:pk>/', views.CustomerDelete.as_view(), name='customer_delete'),
    path('users_docs_list/', views.UsersDocsList.as_view(), name='users_docs_list'),
    # path('users_docs_add/<int:pk>/', views.UsersDocsAdd.as_view(), name='users_docs_add'),
    path('users_docs_delete/<int:pk>/', views.UsersDocsDelete.as_view(), name='users_docs_delete'),
    # path('', views.DocumentsJournalList.as_view(), name='documents_journal'),
]
