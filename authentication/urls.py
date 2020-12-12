from django.urls import path

from authentication import views

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]