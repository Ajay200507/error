from django.urls import path
import apiApp.views as v

urlpatterns = [
    path('login',v.login,name='login'),
    path('create_user',v.create_user,name='create_user'),
    path('create_todo',v.create_todo,name='create_todo'),
    path('intial_call',v.intial_call,name='intial_call'),
    path('completed',v.completed,name='completed'),
    path('in_progress',v.in_progress,name='in_progress'),
    path('archived',v.archived,name='archived'),

]