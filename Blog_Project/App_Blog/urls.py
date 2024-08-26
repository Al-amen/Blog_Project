from django.urls import path,include
from App_Blog import views

app_name = "App_Blog"

urlpatterns = [
    path('blog_list',views.BlogList.as_view() , name= 'blog_list'),
    path('write/',views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>',views.liked, name="liked_post"),
    path('unliked/<pk>',views.unliked, name="unliked_post")
    
    
]
