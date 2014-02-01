from django import forms
from models import Blog

#class postForm(forms.Form):  
    #title = forms.CharField(max_length=100, unique=True)
    #slug = forms.SlugField(max_length=100, unique=True)
    #body = forms.TextField()
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Blog