from django.shortcuts import render,redirect

def instagram(request):
    return redirect('https://www.instagram.com/gehubloodportal')

def facebook(request):
    return redirect('https://www.facebook.com/gehubloodportal')

def twitter(request):
    return redirect('https://www.twitter.com/gehubloodportal')

