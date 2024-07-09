from django.contrib import admin
from App_Blog import models
# Register your models here.

admin.site.register(models.Blog)
admin.site.register(models.Comment)
admin.site.register(models.Likes)