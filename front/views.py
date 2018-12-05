from django.shortcuts import render
from django.http import HttpResponse
from .models import Score,Student,Teacher,Course
from django.db.models import Avg,Sum,Count
from django.db import connection

def index(request):
    #1、查询平均成绩大于60分的同学的ID和平均成绩
    #__gt大于、__gte大于等于、__lt小于、__lte小于等于
    students = Student.objects.annotate(score_avg=Avg("score__number")).filter(score_avg__gt=60).values('id','score_avg')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse("success")

def index2(request):
    #2、查询所有同学的ID，姓名，选课的数量，总成绩
    students = Student.objects.annotate(course_count=Count("score"),score_sum=Sum("score__number")).values('id','name','course_count','score_sum')
    for student in students:
        print(student)
    return HttpResponse("index2")

def index3(request):
    #3、查询姓王老师的个数
    teachers = Teacher.objects.filter(name__startswith='王').count()
    # for teacher in teachers:
    print(teachers)
    #     print(teacher)
    return HttpResponse('index3')

#4、查询没学过“李老师”课的同学的ID、姓名
#5、查询学过ID为1和2的所有同学的ID，姓名
#6、查询所有课程成绩小于60分的同学的ID和姓名
