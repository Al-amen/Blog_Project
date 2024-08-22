from django import forms
from App_Blog import models

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = models.Comment
        fields = ("comment",)

      

