from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.shortcuts import HttpResponse
from userportal.models import profile

# Create your views here.

def login(request):

    if request.method == 'POST':
        user_name=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            request.session['user_id'] = user.id
            auth.login(request,user)
            return redirect('/userportal/portal')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/accounts/login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')






def signup(request):

    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        user_name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']

        
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists...')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken...')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                new=profile(user_id=user.id)
                user.save()
                new.save()
                
        else:
            messages.info(request,'password not matching...')
            return redirect('signup')
        return redirect('/accounts/login')
    else:
        return render(request,'signup.html')
