from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.http import HttpResponse, JsonResponse
#from models import Question

from .models import Choice, Question
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
    data = list(Question.objects.values().filter(form_type="Basic"))
    return JsonResponse({'questions': data})


def FollowUpQuestionList(request):
    data = list(Question.objects.values().filter(form_type="Follow-up"))
    return JsonResponse({'questions': data})


def generate_survey_id():
    #random id generator
    import random
    import string
    #create 6 random numbers
    id = ''.join(random.choice(string.digits) for _ in range(6))

    return id  


def survey_injector(request):
    survey_id = generate_survey_id()
    #take post api body part
    #save to db
    #return survey_id

    body = request.body.decode('utf-8')
    body = json.loads(body)
    #extract name from json body
    name = body['name']
    return JsonResponse({'id': survey_id, 'name': name})