from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
    data = list(Question.objects.values().filter(form_type="Basic"))
    return JsonResponse({'questions': data})


def FollowUpQuestionList(request):
    data = list(Question.objects.values().filter(form_type="Follow-up"))
    return JsonResponse({'questions': data})

@csrf_exempt
def post_base_form(request):
    #TODO add baseform into DB
    print(request.body)
    print(request)
    return JsonResponse({"status": "added"})

    