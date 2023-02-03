from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_base_questions/', views.get_base_questions, name="get_base_questions"),
    path('baseQuestionList/', views.baseQuestionList, name='baseQuestionList'),
    path('FollowUpQuestionList/', views.FollowUpQuestionList, name='FollowUpQuestionList'),

    path('survey_injector/', views.survey_injector, name='survey_injector'),
    path('survey_injecttor_follow_up/', views.survey_injecttor_follow_up, name='survey_injector_follow_up'),
    path('answeredBaseQuestionList/', views.answeredBaseQuestionList, name='answeredBaseQuestionList')

]