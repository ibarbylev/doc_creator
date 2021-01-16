from django.urls import path

from docs import views

urlpatterns = [
    path('', views.DocsListIndex.as_view(), name='index'),
    path('docs/<int:pk>/', views.DocsDetailsIndex.as_view(), name='doc_details'),
    path('docs/<int:pk>/', views.DocsDetailsForUsersIndex.as_view(), name='doc_details_for_users'),
    path('docs/create/', views.DocsCreateView.as_view(), name='doc_create'),
    path('docs/update/<int:pk>/', views.DocsUpdateView.as_view(), name='doc_update'),
    path('docs/delete/<int:pk>/', views.DocsDeleteView.as_view(), name='doc_delete'),
    path('docs/purchase_request/<int:pk>/', views.TemplatePurchaseRequest.as_view(), name='doc_purchase_request'),
]
