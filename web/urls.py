from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^postTodo/?$', views.postTodo, name = 'postTodo'),
    url(r'^TodoPages$', views.TodoPage, name='TodoPages'),
    url(r'^TodoPages/$', views.TodoPage, name='TodoPages'),
]
