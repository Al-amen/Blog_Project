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
    
    
@login_required

def blog_details(request,slug):
    
     blog = models.Blog.objects.get(slug=slug)
     comment_form = forms.CommentForm()
     if request.method == 'POST':
         comment_form = forms.CommentForm(request.POST)
         comment = comment_form.save(commit=False)
         comment.user = request.user
         comment.blog = blog
         comment.save()
         return  HttpResponseRedirect(reverse('App_Blog:blog_details',kwargs={'slug':slug} ))
         
     context={
        'blog': blog,
        'comment_form':comment_form
    }    
     return render(request, "App_Blog/blog_details.html", context=context)
    