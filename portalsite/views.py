from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')

def gallary(request):
    return render(request,'gallary.html')

def about(request):
    return render(request,'aboutus.html')

'''

def instagram(request):
    return redirect("https://www.instagram.com/gehubloodportal")

def facebook(request):
    return redirect("https://www.facebook.com/gehubloodportal")

def twitter(request):
    return redirect("htttps://www.twitter/gehubloodportal")'''