from django.urls import path

from App_Login import views

app_name = "App_Login"

urlpatterns = [
    
    path("signup/",views.sign_up, name="signup"),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('profile/',views.user_profile, name='profile'),
    path('change_profile/',views.user_profile_change, name='change_profile'),
    path('password/', views.pass_change, name='pass_change'),
    path('add-picture/', views.pro_pic_add, name = "pro_pic_add"),
    path('change-picture/',views.change_pro_pic, name= 'change_pro_pic'),

]
