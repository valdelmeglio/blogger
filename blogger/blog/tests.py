"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from blogger.blog.models import Blog, Category
'''
class BlogPostFactory(object):
    def create(self, save=False):
        category = Category()
        category.title = "categoria prova"
        category.slug = "categoria prova"
        blogpost = Blog()
        blogpost.title = "TestPost"
        blogpost.slug  ="TestPost"
        blogpost.body = "This is a test"
        blogpost.category = category
        
        if save==True:
            blogpost.save()

        return blogpost
 '''       
class CategoryFactory(object):
    def create(self, save=False):
        category = Category()
        category.title = "categoria prova"      
        category.slug = "categoria prova"
        
        if save==True:
            category.save()

        return category
        
                
            
class BlogTest(TestCase):
    def setUp(self):
        pass
    '''
    def test_post_creation(self):
        blogpost = BlogPostFactory().create(True)
        self.assertTrue(blogpost.id > 0, "BlogPost created correctly")
    '''
    def test_category_creation(self):
        category = CategoryFactory().create(True)
        self.assertTrue(category.id > 0, "Category created correctly")