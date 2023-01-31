from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse, JsonResponse
#from models import Question

from .models import Choice, Question, FilledQuestionair
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_base_questions(request, *args, **kwargs):
    print(request.GET)
    return JsonResponse(
        {"questions":[
            {
                "id": 1,
                "pl": "Czy twoje dziecko jest głuche?",
                "en": "Is your child deaf",
                "pass_choice": False
            },
            {
                "id": 2,
                "pl": "Czy twoje dziecko jest niewidome?",
                "en": "Is your child blind",
                "pass_choice": True
            }
        ]
        }
    )


def baseQuestionList(request):
    data = list(Question.objects.values().filter(form_type="BASIC"))
    return JsonResponse({'questions': data})


def FollowUpQuestionList(request):
    data = list(Question.objects.values().filter(form_type="FOLLOW_UP"))
    print(request.GET['questionare_id'])
    return JsonResponse({'questions': data})


def generate_survey_id():
    #random id generator
    import random
    import string
    #create 6 random numbers
    id = ''.join(random.choice(string.digits) for _ in range(6))

    return id  

@csrf_exempt
def survey_injector(request):
    questionair_id = generate_survey_id()
    #take post api body part
    #save to db
    #return survey_id

    body = request.body.decode('utf-8')
    body = json.loads(body)["base_form_data"]
    
    post_code = body['post_code']
    month_of_birth = body['month_of_birth']
    year_of_birth = body['year_of_birth']
    date_of_birth = body['date_of_birth']
    score = body['score']

    #save to db
    FilledQuestionair.objects.all()
    db_injection = FilledQuestionair(questionair_id=questionair_id, post_code=post_code, month_of_birth=month_of_birth, year_of_birth=year_of_birth, score=score, date_of_birth=date_of_birth)
    db_injection.save()

    return JsonResponse({'questioner_id': questionair_id, 'post_code': post_code, 'month_of_birth': month_of_birth, 'year_of_birth': year_of_birth, 'score': score})

def survey_injecttor_follow_up(request, questionair_id):
    #check if survey_id exists
    
    try:
        #questionair_id = request.GET['questionair_id']
        FilledQuestionair.objects.get(questionair_id=questionair_id)
        return JsonResponse({'questionair_id': questionair_id})

    except FilledQuestionair.DoesNotExist:
        return JsonResponse({'error': 'questionair_id not found'})

    #if exists, save to db
    #if not, return error
