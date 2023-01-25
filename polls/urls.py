from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_base_questions/', views.get_base_questions, name="get_base_questions")
]