from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

course_dictonary={
    "python":"Python Course",
    "C_Sharp":"C# Course",
    "kotlin":"Kotlin Course"
}
# Create your views here.
def index(request):
    return HttpResponse("Selam")

def course(request,item):
    #buda olur
   # return HttpResponse(course_dictonary[item])

    try:

        #bu da olur. try catch gerek kalmadan, default çıkar, listede olmayan
        #return HttpResponse(course_dictonary.get(item,"Default olarak Not Found"))
    
        # bu da olur. Bu 

        courseitem=course_dictonary[item]
        return HttpResponse(courseitem)

    except:
         # bu ise settings'te debug modu false olursa açılır.
         return HttpResponseNotFound("Sayfa YOKKKK")

def multiply(request,num1,num2):
    return HttpResponse(f"{num1}*{num2}={num1*num2}")