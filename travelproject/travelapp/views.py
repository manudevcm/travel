from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    # return HttpResponse("<h1>hello world</h1>")                (for simple html)
    return render(request,"registation.html")

def about(request):
    return render(request,"login.html")

def contact(request):
    return HttpResponse("hello this contact page")

#new vedio

def demonew(request):
    name="india"
    name2="you"
    return render(request,"about.html",{'obj':name,'obj1':name2})

#nwe vedio
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    plus=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return render(request,'result.html',{'a':plus,'b':sub,'c':mul,'d':div,'p':x,'q':y})

def demoweb(request):
    obj=place.objects.all()
    onj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':onj2})