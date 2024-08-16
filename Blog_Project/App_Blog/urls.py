from django.urls import path
from App_Blog import views
app_name = "App_Blog"
urlpatterns = [
    path('blog_list',views.index , name= 'blog_list'),
    path('write/',views.CreateBlog.as_view(), name='create_blog'),
    
]
