from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm




def acc_signup(request):

        if request.method == 'POST':
                form = UserCreationForm(request.POST)

                if form.is_valid():
                        user = form.save()
                        login(request,user)
                        return redirect('articles_home')

        else :
                form = UserCreationForm()
        return render(request, 'signup.html', {'form' : form})

def acc_login(request):
        if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                        user = form.get_user()
                        login(request,user)
                        if 'next' in request.POST :
                                return redirect(request.POST.get('next'))
                        else :
                                return redirect('articles_home')

                        
        else:
                form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})

def acc_logout(request):
        
        if request.method == 'GET':
                logout(request)
                return redirect('articles_home')


