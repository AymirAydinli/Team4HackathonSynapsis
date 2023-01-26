from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_base_questions(request, *args, **kwargs):
    print(request.GET)
    return JsonResponse(
        {"questions":[
            {
                "id": 1,
                "pl": "Czy twoje dziecko jest głuche?",
                "en": "Is your child deaf"
            },
            {
                "id": 2,
                "pl": "Czy twoje dziecko jest niewidome?",
                "en": "Is your child blind"
            }
        ]
        }
    )