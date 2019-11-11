from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('supervised_ml/', views.supervised_category, name='supervised_category'),
    path('unsupervised_ml/', views.unsupervised_category, name='unsupervised_category'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('ml_projects/', views.mlprojects, name='mlprojects'),
    path('classification_iris/', views.iris, name='iris'),
    path('regression_salary/', views.salary, name='salary'),
]
