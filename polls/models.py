from django.db import models

# Create your models here.
from datetime import datetime
from datetime import timezone
from django.db import models


class Question(models.Model):

    BASIC = 'BASIC'
    FOLLOW_UP = 'FOLLOW-UP'

    question_no = models.IntegerField()
    question_text_pl = models.CharField(max_length=200)
    question_text_en = models.CharField(max_length=200)
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    
    FORM_TYPE_CHOISE = [(BASIC, 'Basic'), (FOLLOW_UP, 'Follow-up'),]

    form_type = models.CharField(max_length=9,
                  choices=FORM_TYPE_CHOISE)

    pass_choise = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text_pl

    def get_text(self, lang):
        if lang == WebText.LANGUAGE_PL:
            return self.question_text_pl
        elif lang == WebText.LANGUAGE_EN:
            return self.question_text_en
        else :
            return self.question_text_pl

    def was_published_recently(self):
        return self.updated_at >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text_pl = models.CharField(max_length=200)
    choice_text_pl = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text_pl

    def get_text(self, lang):
        if lang == WebText.LANGUAGE_PL:
            return self.choice_text_pl
        elif lang == WebText.LANGUAGE_EN:
            return self.choice_text_pl
        else :
            return self.choice_text_pl

class WebText(models.Model):

    LANGUAGE_PL = 'pl'
    LANGUAGE_EN = 'en'

    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    text_code = models.CharField(max_length=20)
    text_pl = models.CharField(max_length=2000)
    text_en = models.CharField(max_length=2000)

class FollowUpQuestion(models.Model):
    created_at = models.DateTimeField(False, True, editable=False)
    updated_at = models.DateTimeField(True, True, editable=False)
    question_parent = models.ForeignKey(Question, on_delete=models.SET_NULL)
    question_parent = models.ForeignKey(Question, on_delete=models.SET_NULL)

    def get_text(self, lang):
        if lang == self.LANGUAGE_PL:
            return self.text_pl
        elif lang == self.LANGUAGE_EN:
            return self.text_pl
        else :
            return self.text_pl
