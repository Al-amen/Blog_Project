from django.db import models

from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_blog')
    blog_title = models.CharField(max_length= 250, verbose_name='Put a title')
    slug = models.SlugField(unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind ?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-publish_date']
        
    def __str__(self):
        return self.blog_title
 
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_user")
    comment = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment


class Likes(models.Model):
     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="liked_blog") 
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")
     
     def __str__(self):
        return self.user + " likes " + self.blog
    
    