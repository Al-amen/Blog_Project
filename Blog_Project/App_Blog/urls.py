from django.urls import path
from App_Blog import views
app_name = "App_Blog"
urlpatterns = [
    path('blog_list',views.BlogList.as_view() , name= 'blog_list'),
    path('write/',views.CreateBlog.as_view(), name='create_blog'),
    
]
