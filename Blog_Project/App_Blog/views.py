from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import CreateView, UpdateView,DetailView,DeleteView,TemplateView,ListView,View
from App_Blog import models

from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.


def index(request):
    
 return render (request, "App_Blog/blog_list.html" , context={})


class CreateBlog(LoginRequiredMixin,CreateView):
    model = models.Blog
    template_name = "App_Blog/create_blog.html"
    fields = ('blog_title','blog_content','blog_image')


    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-') + '-' + str(uuid.uuid4)
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
        
    