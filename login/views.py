from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

def ver_login(request):
    return render(request, 'login.html')

