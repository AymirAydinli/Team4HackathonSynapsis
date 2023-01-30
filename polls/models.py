from django.db import models

# Create your models here.
from datetime import datetime
from datetime import timezone
from django.db import models

BASIC = 'BASIC'
FOLLOW_UP = 'FOLLOW-UP'

class Question(models.Model):

    question_no = models.IntegerField()
    question_text_pl = models.CharField(max_length=200)
    question_text_en = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True, editable=False)
    question_parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='question_children')
    follow_up_answer = models.BooleanField(default=False, null=True)
    
    FORM_TYPE_CHOISE = [(BASIC, 'Basic'), (FOLLOW_UP, 'Follow-up'),]

    form_type = models.CharField(max_length=9,
                  choices=FORM_TYPE_CHOISE)

    pass_choice = models.BooleanField(null=True)

    def __str__(self):
        return self.question_text_pl

    def was_published_recently(self):
        return self.updated_at >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text_en = models.CharField(max_length=200)
    choice_text_pl = models.CharField(max_length=200)
    pass_choice = models.BooleanField(null=True)

    def __str__(self):
        return self.choice_text_pl


class WebText(models.Model):

    LANGUAGE_PL = 'pl'
    LANGUAGE_EN = 'en'

    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True, editable=False)
    text_code = models.CharField(max_length=20)
    text_pl = models.CharField(max_length=2000)
    text_en = models.CharField(max_length=2000)

    def __str__(self):
        return self.choice_text_pl


# class FollowUpQuestion(models.Model):
#     created_at = models.DateTimeField(auto_now_add = True, editable=False)
#     updated_at = models.DateTimeField(auto_now = True, editable=False)
#     question_parent = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
#     question_follow_up = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='question_follow_up_id')
#     follow_up_answer = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True)

class FilledQuestionair(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True, editable=False)
    post_code = models.CharField(max_length=6, null=False)
    month_of_birth = models.IntegerField()
    year_of_birth = models.IntegerField()
    date_of_birth = models.DateField(null=True)
    questionair_id = models.IntegerField(null=False, unique=True)
    score = models.IntegerField(null=False)

class QustionAnswer(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, editable=False)
    updated_at = models.DateTimeField(auto_now = True, editable=False)
    
    quistionair = models.ForeignKey(FilledQuestionair, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True)
    answer_value = models.BooleanField(null=True)
    custom_answer = models.CharField(max_length=2000)


