# Create your views here.

from blogger.blog.models import Blog, Category, BlogComment
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from forms import PostForm, CommentForm, NewCategory
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# twitter APIs
import twitter
from twitter_api_keys import *

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()},
        context_instance=RequestContext(request))

def view_post(request, id):
    post = Blog.objects.get(id = int(id))
    comments = BlogComment.objects.filter(post = post)
    context = {'post': post, 'comments': comments, 'form': CommentForm()}
    return render(request, 'view_post.html', context) 
'''       
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })
'''
    
@login_required
def view_form(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/')
    
    context = {'form': form}
    return render_to_response('view_form.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))
                              
@login_required
def edit_post(request, id):
    if request.POST:
        post = get_object_or_404(Blog, pk=id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/') 
    else: 
        post = get_object_or_404(Blog, pk=id)
        form = PostForm(instance=post)
        context = {'form': form, 'post': post}
        #return render(request, 'view_form.html', context)
        return render_to_response('view_form.html', 
                             {'form': form, 'post': post},
                              context_instance=RequestContext(request))    
                              
@login_required
def delete_post(request, id):
    # to improve
    post = Blog.objects.get(id = int(id)) 
    post.delete()  
    return HttpResponseRedirect('/') 


def add_comment(request, id):
    form = CommentForm(request.POST)
    
    if form.is_valid():
        post = Blog.objects.get(id=id)
        form.save(post = post)
        return HttpResponseRedirect('/')

@login_required
def delete_comment(request, id):
    # to improve
    postComment = BlogComment.objects.get(id = int(id)) 
    postComment.delete()  
    return HttpResponseRedirect('/') 
    
def view_categories(request):
    '''
    return render_to_response('view_categories.html', {
        'categories': Category.objects.all()
    })
    '''
    context = {'categories': Category.objects.all()}
    return render(request, 'view_categories.html', context ) 
    
@login_required
def new_category(request):
    form = NewCategory(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect('/')
    
    context = {'form': form}
    return render_to_response('new_category.html', 
                              { 'form': form },
                              context_instance=RequestContext(request))
                              
                              
def category_post(request, title):
    category = get_object_or_404(Category, title=title)
    return render_to_response('index.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })
                               
                                
                                