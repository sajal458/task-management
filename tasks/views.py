from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return HttpResponse("welcome")
    
def show_task(request):
    return HttpResponse("this is show")
def show_specific_task(request,id):
    print("id",id)
    print("id type",type(id))
    return HttpResponse(f"this is specific task {id}")