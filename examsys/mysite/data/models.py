from django.db import models
# Create your models here.

#user message
class Student(models.Model):
    num = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    sex = models.BooleanField()
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField(blank = True)
    phone = models.CharField(blank = True,max_length = 11)
    college = models.CharField(max_length = 15,blank = True)
    def __unicode__(self):
        return self.name
class Teacher(models.Model):
    num = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    sex = models.BooleanField()
    age = models.IntegerField()
    birth = models.DateField()
    email = models.EmailField(blank = True)
    phone = models.CharField(max_length = 11,blank = True)
    college = models.CharField(max_length = 15,blank = True)
    subject =models.CharField(max_length=30)
    def __unicode__(self):
        return self.name
#userlog
        
#question and exam
class Question(models.Model):
    num = models.CharField(max_length=15)
    style = models.CharField(max_length = 10)
    diffculty = models.CharField(max_length = 5)
    Qmain = models.TextField()
    ans = models.CharField(max_length = 20)
    data = models.DateField(auto_now= True)
    def __unicode__(self):
        return self.Qmain
    #point = models.CharField(max_length = 30)
class MarkandPos(models.Model):
    question = models.ForeignKey(Question)
    mark = models.IntegerField()
    pos = models.CharField(max_length = 10,blank = True)#can not be blank or null
    def __unicode__(self):
        return self.question.Qmain
class Exam(models.Model):
    num = models.CharField(max_length = 15)    
    subject = models.CharField(max_length=30)
    diffculty = models.CharField(max_length = 5)
    #author = models.ForeignKey(Teacher)
    questions= models.ManyToManyField(MarkandPos,blank = True)        
class Point(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
    questions= models.ManyToManyField(Question,blank = True) 
    def __unicode__(self):
        return self.name
#studentans
class StudentQAns(models.Model):
    student = models.ForeignKey(Student)
    question =models.ForeignKey(Question)
    studentans = models.CharField(max_length = 20)
    correct = models.BooleanField(blank = True)
class StuedntEAns(models.Model):
    student = models.ForeignKey(Student)
    ans  = models.ManyToManyField(StudentQAns)
    mark = models.CharField(max_length = 100,blank = True,null = True)
#ExamModels