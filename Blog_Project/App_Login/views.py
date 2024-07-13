from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form = UserCreationForm()
    register = False
    
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
             form.save()
             register = True
    
    dict = {'form':form, 'register': register}
    
    return render(request, 'App_Login/signup.html', context=dict)


def login_page(request):
    form = AuthenticationForm()
    
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                return HttpResponseRedirect(reverse('index'))
                
    return render(request, 'App_Login/login.html',context={'form':form})
@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index' ))
    