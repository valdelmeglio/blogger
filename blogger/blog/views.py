# Create your views here.

from blogger.blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from forms import PostForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()
    })

def view_post(request, id):
    post = Blog.objects.get(id = int(id))
    context = {'post': post}
    #return render(request, 'view_post.html', context)
    return render_to_response('view_post.html', {'post': post}, context_instance=RequestContext(request)) 
       
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)
    })
    
@login_required
def view_form(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect('/')
    
    context = {'form': form}
    #return render(request,'view_form.html/',context)
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