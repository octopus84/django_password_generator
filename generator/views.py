from django.shortcuts import render
# from django.http import HttpResponse
 
def home(request):
     return render(request, 'home.html')
 
# Create your views here.
def about(request):
    # return '<h1>Hallo Welt</h1>'
    # return HttpResponse('<h1>Hallo Welt</h1>')
    return render(request, 'about.html')

def password(request):
    return render(request,'password.html')