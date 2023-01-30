from django.contrib import admin
from .models import Question
from .models import Choice
# from .models import FollowUpQuestion
from .models import FilledQuestionair
from .models import QustionAnswer


# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
# admin.site.register(FollowUpQuestion)
admin.site.register(FilledQuestionair)
admin.site.register(QustionAnswer)
