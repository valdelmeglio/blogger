from django import forms
from models import Blog, BlogComment

#class postForm(forms.Form):  
    #title = forms.CharField(max_length=100, unique=True)
    #slug = forms.SlugField(max_length=100, unique=True)
    #body = forms.TextField()
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','slug', 'body', 'category']
 
    def clean(self):
        cleaned_data = self.cleaned_data

        if self._errors and 'category' in self._errors:
            raise forms.ValidationError("You call that a title?!")
        else:
            return cleaned_data  
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        exclude = ('post',)

    def save(self, post, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        comment.post = post

        if commit:
            comment.save()
        return comment            