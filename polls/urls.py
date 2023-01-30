from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_base_questions/', views.get_base_questions, name="get_base_questions"),
    path('baseQuestionList/', views.baseQuestionList, name='baseQuestionList'),
    path('FollowUpQuestionList/', views.FollowUpQuestionList, name='FollowUpQuestionList'),

    path('survey_injector/', views.survey_injector, name='survey_injector'),
]