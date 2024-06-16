from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('problems/', views.problems, name='problems'),
    path('problem/', views.index, name='problem'),
    path('problem_1/', views.index_1, name='problem_1'),
    path('index2/', views.index_2, name='problem_2'),
    path('index3/', views.index_3, name='problem_3'),
    path('index4/', views.index_4, name='problem_4'),
    path('index5/', views.index_5, name='problem_5'),
    path('index6/', views.index_6, name='problem_6'),
]
