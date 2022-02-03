from random import choice, random
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
    ####characters
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('special'):
        characters.extend(list('!"#$%&/()=?¡'))
        
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVWXYZ'))        
        
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))        
        
    for x in range(length):
        generated_password += choice(characters)
        
    return render(request,'password.html',{'password': generated_password})