from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import participants,historydonations,profile,event
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login')
def portal(request):
    return render(request,'portal.html')


@login_required(login_url='/accounts/login')
def donate(request):
    user = User.objects.get(username=request.user)
    if user.DoesNotExist:
        if request.method == 'POST':
            username=request.POST['username']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            age=request.POST['age']
            date=request.POST['date']
            bloodgroup=request.POST['bgrp']

            if int(age)>18:
                new=participants(firstname=firstname,lastname=lastname,bloodgroup=bloodgroup,age=age,date=date)
                new.save()
                new1=historydonations(username=username,firstname=firstname,lastname=lastname,bloodgroup=bloodgroup,age=age,date=date)
                new1.save()
                return redirect('/userportal/portal')
            else:
                messages.info('you are not eligible')
                return redirect('/userportal/donate')
        else:
            
            return render(request,'donate.html')
    else:
        return HttpResponse('error 404')


@login_required(login_url='/accounts/login')
def learnaboutdonation(request):
    return render(request,'learnaboutdonation.html')


@login_required(login_url='/accounts/login')
def userprofile(request):
    user=request.user.profile
    form=ProfileForm(instance=user)

    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=user)

        if form.is_valid():
            prof=form.save(commit=False)
            prof.save()

    context={'form':form}
    return render(request,'profile.html',context)










@login_required(login_url='/accounts/login')
def mydonations(request):
    user = User.objects.get(username=request.user)
    data=historydonations.objects.all().filter(username=user)

    return render(request,'Mydonations.html',{'messages':data})


@login_required(login_url='/accounts/login')
def events(request):
    events=event.objects.all()
    return render(request,'eventlist.html',{'eventdata':events})
