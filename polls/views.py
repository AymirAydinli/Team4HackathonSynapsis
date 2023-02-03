from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse, JsonResponse
#from models import Question

from .models import Choice, Question, FilledQuestionair, QustionAnswer
import json
from django.db.models import Prefetch

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

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

def parsQuestionList(query_result):
    data = list()
    for q in query_result:
        choices_set = list()
        for c in q.choices_set.all():
            c_dict = {'id': c.id,
                    'created_at': c.created_at,
                    'updated_at': c.updated_at,
                    'question_id' : c.question_id,
                    'choice_text_en': c.choice_text_en,
                    'choice_text_pl': c.choice_text_pl,
                    'pass_choice': c.pass_choice
            }
            choices_set.append(c_dict)
        q_dict = {'id': q.id,
                'question_no': q.question_no,
                'question_text_pl': q.question_text_pl,
                'question_text_en': q.question_text_en,
                'created_at': q.created_at,
                'updated_at': q.updated_at,
                'question_parent_id': q.question_parent_id,
                'follow_up_answer': q.follow_up_answer,
                'custom_answer': q.custom_answer,
                'form_type': q.form_type,
                'pass_choice': q.pass_choice,
                'frequency_question': q.frequency_question,
                'choices_set': choices_set}
        # print(q_dict)
        data.append(q_dict)
    return data

def answeredBaseQuestionList(request):
    questionare_id = request.GET['questionare_id']
    #follow_up_questions = list(Question.objects.values().filter(form_type="FOLLOW_UP").prefetch_related('choices'))
    filled = list(FilledQuestionair.objects.values().filter(questionair_id=questionare_id))
    answered_questions = list(QustionAnswer.objects.values().filter(quistionair_id=filled[0]["id"]).filter(answer_value=False))

    base_question_id_list = []

    for answ in answered_questions:
        base_question_id_list.append(answ["question_id"])

    print(base_question_id_list)

    base_false_questions = list(Question.objects.values().filter(form_type="BASIC").filter(question_no__in=base_question_id_list))
    return JsonResponse({'questions': base_false_questions})

def FollowUpQuestionList(request):

    # questionare_id = request.GET['questionare_id']
    # #follow_up_questions = list(Question.objects.values().filter(form_type="FOLLOW_UP").prefetch_related('choices'))
    # filled = list(FilledQuestionair.objects.values().filter(questionair_id=questionare_id))
    # answered_questions = list(QustionAnswer.objects.values().filter(quistionair_id=filled[0]["id"]).filter(answer_value=False))

    # follow_up_questions = []
    # for answ in answered_questions:
    #     question = list(Question.objects.values().filter(form_type="BASIC").filter(question_no=answ["question_id"]))[0]
    #     follow_up_questions.append(question)
    #     follow_up_question_level_1 = list(Question.objects.values().filter(form_type="FOLLOW_UP").filter(question_no=question["id"]))
    #     #choices = list(Choice.objects.values().filter(question_id=question["id"]))

    #     print(follow_up_question_level_1)

    # # q = Question.objects.prefetch_related('choices_set').filter(form_type="FOLLOW_UP")[0]
    # # print(q)
    # # print(q.choices_set)
        

    # #print(request.GET['questionare_id'])
    # return JsonResponse({'questions': follow_up_questions})

    questionare_id = request.GET['questionare_id']
    #follow_up_questions = list(Question.objects.values().filter(form_type="FOLLOW_UP").prefetch_related('choices'))
    filled = list(FilledQuestionair.objects.values().filter(questionair_id=questionare_id))
    answered_questions = list(QustionAnswer.objects.values().filter(quistionair_id=filled[0]["id"]).filter(answer_value=False))

    base_question_id_list = []

    for answ in answered_questions:
        base_question_id_list.append(answ["question_id"])

    print(base_question_id_list)

    base_false_questions = list(Question.objects.values().filter(form_type="BASIC").filter(question_no__in=base_question_id_list))

    query_result = Question.objects.filter(form_type="FOLLOW_UP").prefetch_related(Prefetch('choices_set'))
    follow_up_questions = parsQuestionList(query_result)

    filtered_follow_up_questions = []
    for answ in answered_questions:
        for foll_up in follow_up_questions:
            if foll_up["question_no"] == answ["question_id"]:
                filtered_follow_up_questions.append(foll_up)


        # question = list(Question.objects.values().filter(form_type="BASIC").filter(question_no=answ["question_id"]))[0]
        
        # follow_up_question_level_1 = list(Question.objects.values().filter(form_type="FOLLOW_UP").prefetch_related(Prefetch('choices_set')).filter(question_no=question["id"]))
        # follow_up_questions.append(follow_up_question_level_1)

    aaa = {"data":[{'questions': base_false_questions}, {'follow_up': follow_up_questions}]}
    #print(aaa)

    # return JsonResponse({"data":[{'questions': base_false_questions}, {'follow_up': follow_up_questions}]})
    return JsonResponse({'follow_up': follow_up_questions})

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
    body = request.body.decode('utf-8')
    body = json.loads(body)["base_form_data"]
    post_code = body['post_code']
    month_of_birth = body['month_of_birth']
    year_of_birth = body['year_of_birth']
    date_of_birth = body['date_of_birth']
    score = body['score']

    #save to db
    filledQuestionair = FilledQuestionair(questionair_id=questionair_id, post_code=post_code, month_of_birth=month_of_birth, year_of_birth=year_of_birth, score=score, date_of_birth=date_of_birth)
    filledQuestionair.save()

    try:
        for idx, answer in enumerate(body['answers']):
            if answer != None:
                qustionAnswer = QustionAnswer(   
                    quistionair=filledQuestionair, 
                    question_id=idx,
                    answer_value=answer, 
                    custom_answer=""
                                    )
                qustionAnswer.save()
    except Exception as e:
        print(e)
    return JsonResponse({'questioner_id': questionair_id, 'post_code': post_code, 'month_of_birth': month_of_birth, 'year_of_birth': year_of_birth, 'score': score})

@csrf_exempt
def survey_injecttor_follow_up(request):
    #check if survey_id exists
    
    try:
        print(request.GET.keys())

        questionair_id = request.GET['questionare_id']
        FilledQuestionair.objects.get(questionair_id=questionair_id)

        body = request.body.decode('utf-8')
        print(body)

        body = json.loads(body)["base_form_data"]
        for k in body.keys() :
            print("[{}] : {}".format(k, body[k]))

        quistionair = questionair_id
        question = body["question"]
        answer = body["answer"]
        answer_value = body["answer_value"]
        custom_answer = body["custom_answer"]

        db_injection = QustionAnswer(   quistionair=FilledQuestionair.objects.get(questionair_id = questionair_id), 
                                        question=Question.objects.get(question_text_pl = question), 
                                        answer=Choice.objects.get(choice_text_pl = answer), 
                                        answer_value=answer_value, 
                                        custom_answer=custom_answer
                                    )
        db_injection.save()

        return JsonResponse({'quistionair': quistionair, 'question': question, 'answer': answer, 'answer_value': answer_value, 'custom_answer': custom_answer})
    
    except FilledQuestionair.DoesNotExist:
        return JsonResponse({'error': 'questionair_id not found'})

    #if exists, save to db
    #if not, return error

def printSummary(request):

    questionair_id = request.GET['questionare_id']
    filledQuestionair = FilledQuestionair.objects.get(questionair_id=questionair_id)

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize='A4')
    p.setFont('Helvetica', 12)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(60, 700, "Drogi Rodzicu!")
    p.drawString(60, 670, "Wynik Twojego Dziecka: {} / 20 punktów.".format(filledQuestionair.score))
    p.drawString(60, 650, "Identyfikator Twojego badania wykonanego {} to: {}".format(filledQuestionair.created_at, questionair_id))
    if filledQuestionair.score < 3:
        p.drawString(60, 620, "Jest nam bardzo milo poinformowac, ze rozwoj Twojego Malucha w zakresie umiejetnosci")
        p.drawString(60, 600, "spoleczno-komunikacyjnych nie budzi niepokoju. Istnieje niskie ryzyko wystapienia")
        p.drawString(60, 580, "spektrum autyzmu.")
        p.drawString(60, 550, "Pamietaj jednak, ze kwestionariusz M-CHAT-R jest jedynie wstepnym badaniem")
        p.drawString(60, 530, "przesiewowym, a nie narzedziem diagnostycznym. Jesli mimo wszystko niepokoi Cie rozwój")
        p.drawString(60, 510, "Twojego dziecka, skontaktuj sie ze specjalista.")

        p.drawString(60, 480, "Pamietaj:")
        p.drawString(60, 460, " 1. Jesli Twoje dziecko w chwili badania nie ukonczylo jeszcze 24 miesiecy, zalecane jest")
        p.drawString(60, 440, "     powtorne wypelnienie kwestionariusza M-CHAT-R pomiedzy 24 a 30 miesiacem zycia.")
        p.drawString(60, 420, " 2. Mozesz skorzystac z bezplatnej teleporady w ramach kontraktu z NFZ.")
        p.drawString(60, 400, "     W celu umowienia sie wypelnij ankiete: https://ankieta.synapsis.waw.pl/ankieta/ ")
        p.drawString(60, 380, " 3. Wiecej informacji na temat umiejetnosci, ktore dziecko w tym wieku powinno posiadac")
        p.drawString(60, 360, "     oraz wspierania jego rozwoju znajdziesz na stronie:")
        p.drawString(60, 340, "     http://badabada.pl/dla-rodzicow/rozwoj-dziecka")
    elif filledQuestionair.score < 8:
        p.drawString(60, 620, "Chcielibysmy poinformowac, ze badanie Twojego Malucha wykazuje pewne")
        p.drawString(60, 600, "nieprawidlowosci w zakresie rozwoju, ktore wskazuja na srednie ryzyko wystepowania")
        p.drawString(60, 580, "spektrum autyzmu u Twojego dziecka.")
        p.drawString(60, 550, "Pamietaj jednak, ze kwestionariusz M-CHAT-R jest jedynie wstepnym badaniem przesiewowym.")
        p.drawString(60, 530, "Dlatego byloby wazne, abys skontaktowal sie ze specjalista. W niektorych przypadkach")
        p.drawString(60, 510, "po takiej rozmowie okazuje sie, ze nie ma powodów do niepokoju o rozwoj dziecka,")
        p.drawString(60, 490, "a w innych, ze potrzebna jest jednak specjalistyczna konsultacja lub diagnoza dziecka.")

        p.drawString(60, 460, "Co mozesz teraz zrobic:")
        p.drawString(60, 440, " 1. Skontaktuj sie ze specjalista (lekarzem, psychologiem, pedagogiem), aby porozmawiac")
        p.drawString(60, 420, "     i omowic wyniki badania oraz wyjasnic swoje watpliwosci")
        p.drawString(60, 400, " 2. Mozesz skorzystac z bezplatnej teleporady w ramach kontraktu z NFZ.")
        p.drawString(60, 380, "     W celu umowienia sie wypelnij ankiete: https://ankieta.synapsis.waw.pl/ankieta/ ")
        p.drawString(60, 360, " 3. Wiecej informacji na temat umiejetnosci, ktore dziecko w tym wieku powinno posiadac")
        p.drawString(60, 340, "     oraz wspierania jego rozwoju znajdziesz na stronie:")
        p.drawString(60, 320, "     http://badabada.pl/dla-rodzicow/rozwoj-dziecka")
    else :
        p.drawString(60, 620, "Chcielibysmy poinformowac, ze rozwój Twojego Malucha przebiega nietypowo, a wynik")
        p.drawString(60, 600, "badania wskazuje wysokie ryzyka wystapienia u niego spektrum autyzmu.")

        p.drawString(60, 570, "Pamietaj jednak, ze kwestionariusz M-CHAT-R jest jedynie wstepnym badaniem przesiewowym,")
        p.drawString(60, 550, "a nie narzedziem diagnostycznym. Dlatego bardzo wazne jest, abys skonsultowal sie ze")
        p.drawString(60, 530, "specjalista zajmujacym sie diagnozowaniem spektrum autyzmu u dzieci. Podczas rozmowy")
        p.drawString(60, 510, "wyjasnisz swoje watpliwosci, uzyskasz porade oraz wskazowki odnosnie dalszych dzialan.")

        p.drawString(60, 480, "Pamietaj:")
        p.drawString(60, 460, " 1. Jesli Twoje dziecko w chwili badania nie ukonczylo jeszcze 24 miesiecy, zalecane jest")
        p.drawString(60, 440, "     powtorne wypelnienie kwestionariusza M-CHAT-R pomiedzy 24 a 30 miesiacem zycia.")
        p.drawString(60, 420, " 2. Mozesz skorzystac z bezplatnej teleporady w ramach kontraktu z NFZ.")
        p.drawString(60, 400, "     W celu umowienia sie wypelnij ankiete: https://ankieta.synapsis.waw.pl/ankieta/ ")

        p.drawString(60, 380, " 3. W oczekiwaniu na konsultacje ze specjalista lub diagnoze:")
        p.drawString(60, 360, "     - prowadz notatki o zdobywanych przez dziecko umiejetnosciach i zachowaniach,")
        p.drawString(60, 340, "         ktore Cie niepokoja")
        p.drawString(60, 320, "     - nagrywaj swoje dziecko podczas zabawy, w kontakcie z osobami bliskimi i innymi dziecmi")
        p.drawString(60, 300, "     - zglos sie do swojej rejonowej Poradni Psychologiczno-Pedagogicznej")

        p.drawString(60, 280, " 4. Wiecej informacji na temat umiejetnosci, ktore dziecko w tym wieku powinno posiadac")
        p.drawString(60, 260, "     oraz wspierania jego rozwoju znajdziesz na stronie:")
        p.drawString(60, 240, "     http://badabada.pl/dla-rodzicow/rozwoj-dziecka")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')