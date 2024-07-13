from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

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