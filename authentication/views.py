from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request,'authentication/index.html' )


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', False)
        fname = request.POST.get('fname', False)
        lname = request.POST.get('lname', False)
        email = request.POST.get('email', False)
        pass1 = request.POST.get('pass1', False)
        pass2 = request.POST.get('pass2', False)

        # myuser = User.objects.create_user(username, email, pass1)
        # myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.save()

        user = User(email = email, username= username, password =pass1)
        user.save()

        messages.success(request, "Your Account has been created succesfully!! ")
        return redirect('signin')
    return render(request, 'authentication/signup.html')



def signin(request):
    return render(request,'authentication/signin.html' )

def signout(request):
    pass