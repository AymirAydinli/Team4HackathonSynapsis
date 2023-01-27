from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
#from models import Question

from .models import Choice, Question

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
    data = list(Question.objects.values())
    return JsonResponse({'questions': data})
