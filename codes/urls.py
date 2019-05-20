from django.urls import path

from . import views

app_name = 'codes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_index>/', views.detail, name = 'detail'),
    path('<int:question_index>/user_rating/', views.user_rating, name = 'user_rating'),
]
