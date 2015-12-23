#from django.template.loader import get_template
#from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from data.models import*
#var
global exam#addexam flag
global pagenum# 
#mathods
def display(points):
    display_list = []
    for point in points:
        display_list.append(point.name)
        children = point.children.all()
        if len(children) > 0:
            display_list.append(display(point.children.all()))
    return display_list
def FindAllChildren(points):
    childlist = list('')
    for point in points:
        childlist.append(point)
        childs = point.children.all()
        if len(childs) > 0:
            childlist += FindAllChildren(point.children.all())
    return childlist
#views
'''def question_readin(request):
    return render_to_response('question_readin.html')'''
def unordered_list(request):
    points = Point.objects.filter(parent=None)
    var = display(points)
    return render_to_response('unordered_list.html', {'var': var})   
#question part
def question_readin(request):
    if 'submit' in request.GET :    
        if 'style' in request.GET:
            message = request.GET['style']
        else:
            message = 'input style please!'
        if 'point' in request.GET:
            message = request.GET['point']
        else:
            message += 'input point please!'
        if 'diffculty' in request.GET:
            message +=request.GET['diffculty']
        else:
            message+='input diffcult please!'
        if 'Qmain'in request.GET:
            message += request.GET['Qmain']
        else:
            message += 'input Qmain please!'
        point = Point.objects.get(name=request.GET['point'])
        if point:
            message='exsit'+ point.name
        else:
            message = 'not exsit'
        Q = Question(style = request.GET['style'],diffculty = request.GET['diffculty'],
                     Qmain = request.GET['Qmain'],ans = request.GET['ans'])
        Q.save()
        point.questions.add(Q)
        return HttpResponse(message)
    else:
        points = Point.objects.all()
        return render_to_response('question_readin.html',{'points':points})
def QuestionView(request):
    global pagenum
    if 'search' in request.GET:
        point = Point.objects.filter(name =  request.GET['subject'])
        childlist = FindAllChildren(point)
        questions = []
        for child in childlist:
            questions+=child.questions.all()
    else:
        questions = Question.objects.all()
    if 'nextpage' in request.GET:
        pagenum = pagenum + 1
    elif 'pagejump' in request.GET:
        pagenum = int(request.GET['pagejump'])
    else:
        pagenum = 1
    if len(questions) % 3 == 0:
        maxjump = len(questions)/3
    else:
        maxjump = len(questions)/3 + 1
    jumplist = list('')
    for i in range(1,maxjump+1):
        jumplist.append(i)
    questions = questions[0+3*(pagenum-1):3+3*(pagenum-1)]
    subjects =  Point.objects.filter(parent = None)
    #return render_to_response('QuestionView.html',{'questions':questions,'pagenum':pagenum,
                                                    #'jumplist':jumplist})
    return render_to_response('QuestionView.html',locals())
#exam part
def AddExam(request):
    global exam
    if 'addexam' in request.GET:
        exam = Exam(subject = request.GET['subject'],diffculty =request.GET['diffculty'])
        exam.save()
        questions = Question.objects.all()
        return render_to_response('QuestionView.html',{'exam':exam,'questions':questions})
    else:
        subjects = Point.objects.filter(parent = None)
        return render_to_response('addexam.html',{'subjects':subjects})
def QuestionSelectResult(request):
    global exam
    resultlist = list('')
    for i in range(0,10):
        if str(i) in request.GET:
            question = Question.objects.get(id = request.GET[str(i)])
            resultlist.append(question)
            mark =  MarkandPos(mark = 10,question = question)
            mark.save()
            exam.questions.add(mark)
    return render_to_response('result.html',{'exam':exam,'results':resultlist})                                                                                                               
#user part
def StudentRegester(request):
    if 'submit' in request.GET:
        student = Student(name = request.GET['name'],num = request.GET['num'],sex =request.GET['age'],
                          college = request.GET['college'],email = request.GET['email'],
                            age =request.GET['age'] ,birth = request.GET['birth'])
        student.save()
        return render_to_response('Regester.html',{'student':student})
        return HttpResponse(birthday)
    else:
        return render_to_response('Regester.html',{'studentregester':True})
def TeacherRegester(request):
    if 'submit' in request.GET:
        teacher = Teacher(name = request.GET['name'],num = request.GET['num'],sex =request.GET['age'],
                          college = request.GET['college'],email = request.GET['email'],
                            age =request.GET['age'] ,birth = request.GET['birth'],
                            subject = request.GET['subject'],phone = request.GET['phone'])
        teacher.save()
        return render_to_response('Regester.html',{'teacher':teacher})
        return HttpResponse(birthday)
    else:
        return render_to_response('Regester.html',{'teacherregester':True})  
def test(request):
    point = Point.objects.get(id = 1)
    questions = point.questions.all()
    return render_to_response('test.html',locals())