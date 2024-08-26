from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, UpdateView,DetailView,DeleteView,TemplateView,ListView,View
from App_Blog import models

from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from App_Blog import forms
# Create your views here.




class CreateBlog(LoginRequiredMixin,CreateView):
    model = models.Blog
    template_name = "App_Blog/create_blog.html"
    fields = ('blog_title','blog_content','blog_image')


    def form_valid(self,  form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-') + '-' + str(uuid.uuid4)
        blog_obj.save()
        
        return HttpResponseRedirect(reverse('index'))
        
    
class BlogList(ListView):
    model = models.Blog
    context_object_name = 'blogs'
    template_name='App_blog/blog_list.html'
    # queryset = models.Blog.objects.order_by('-publish_date')


class MyBlog(LoginRequiredMixin,TemplateView):
    template_name = "App_Blog/my_blog.html"

   
@login_required
def blog_details(request,slug):
    
     blog = models.Blog.objects.get(slug=slug)
     comment_form = forms.CommentForm()
     liked = False
     already_liked = models.Likes.objects.filter(blog=blog,user=request.user)
     if already_liked:
         liked = True
     else:
         liked = False
     if request.method == 'POST':
         comment_form = forms.CommentForm(request.POST)
         comment = comment_form.save(commit=False)
         comment.user = request.user
         comment.blog = blog
         comment.save()
         return  HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':slug} ))
         
     context={
        'blog': blog,
        'comment_form':comment_form,
        'liked':liked
    }    
     return render(request, "App_Blog/blog_details.html", context=context)

@login_required
def liked(request, pk):
    blog = models.Blog.objects.get(pk=pk)
    print(pk)
    user = request.user
    already_liked = models.Likes.objects.filter(blog=blog,user=user)
    
    if not already_liked:
        liked_post = models.Likes(blog=blog,user=user)
        liked_post.save()  
        print(blog.slug)   
        return  HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug} ))

@login_required

def unliked(request,pk):
    blog = models.Blog.objects.get(pk=pk)
    user = request.user
    already_liked = models.Likes.objects.filter(blog=blog,user=user)
    
    already_liked.delete()
    return  HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':blog.slug} ))
    
    

class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Blog
    fields = ('blog_title','blog_content','blog_image')
    template_name = "App_Blog/edit_blog.html"
      
    def get_success_url(self, **kwargs):
       
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug': self.object.slug})
    