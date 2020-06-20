from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def Home(request):
    #return HttpResponse('Hello this is my home page')
    #{'password':'adadadasfsf6749*'} bir dictionary, olusturacagimiz password u sayfaya yazdirmak icin boyle kullaniyoruz.
    return render(request,'generator/home.html',{'password':'adadadasfsf6749*'})

def Eggs(request):
    return HttpResponse('<h1>This is egg page</h1>')

def Password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOQPRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@#&*.,{}()^<>?'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword +=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

#About page view
def About(request):
    return render(request, 'generator/about.html')
