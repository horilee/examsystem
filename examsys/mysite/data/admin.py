from django.contrib import admin

# Register your models here.
from data.models import*
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Point)
admin.site.register(MarkandPos)
admin.site.register(StudentQAns)
admin.site.register(StuedntEAns)
