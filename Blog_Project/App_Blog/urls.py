from django.urls import path
from App_Blog import views
app_name = "App_Blog"
urlpatterns = [
    path('blog_list',views.index , name= 'blog_list')
]
