from django.urls import path

from App_Login import views

app_name = "App_Login"

urlpatterns = [
    
    path("signup/",views.sign_up, name="signup"),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),

]
