from django.contrib import admin

from django.urls import path


from blog.views import blog_view,blog_detail
urlpatterns = [
    path('', blog_view ,name='allblogs'), 
     path('<int:blog_id>/', blog_detail ,name='details'), 
]
