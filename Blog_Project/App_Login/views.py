
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App_Login import forms

def sign_up(request):
    form = forms.SignUpForm()
    register = False
    
    if request.method == "POST":
        form = forms.SignUpForm(data=request.POST)
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


@login_required

def user_profile(request):
    
    return render(request, 'App_Login/profile.html',context={})

@login_required

def user_profile_change(request):
    current_user = request.user
    form = forms.UserProfileChange(instance=current_user,)
    print(current_user.id)
    if request.method == "POST":
        form = forms.UserProfileChange(request.POST , instance=current_user,)
        if form.is_valid():
            form.save()
            form = forms.UserProfileChange(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
            
    return render(request, 'App_Login/change_profile.html',context={'form':form})

@login_required

def pass_change(request):
    change = False
    
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            change = True
              # Redirect back to the same page after successful password change
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'App_Login/pass_change.html', {'form': form, 'change': change})

@login_required

def pro_pic_add(request):
    form = forms.ProfilePic()
    if request.method == 'POST':
        form = forms.ProfilePic(request.method, request.FILES)
        if form.is_valid():
           user_obj =  form.save(commit=False)
           user_obj.user = request.user
           user_obj.save()
           return HttpResponseRedirect(reverse('App_Login:profile', ))
           
    return render(request, 'App_Login/pro_pic_add.html',context={'form':form})

@login_required

def change_pro_pic(request):
    form = forms.ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = forms.ProfilePic(request.method, request.FILES, instance=request.user.user_profile)
        form.save()
        return HttpResponseRedirect(reverse('App_Login:profile', ))
        
    return render(request, 'App_Login/pro_pic_add.html',context={'form':form})