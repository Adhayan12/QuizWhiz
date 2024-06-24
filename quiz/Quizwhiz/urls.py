from django.contrib import admin
from django.urls import path
from Quizwhiz import views
urlpatterns = [
    
    path("", views.index, name='index'),
    path("Quiz2", views.Quiz2, name='Quiz2'),
    path("Options2", views.Options2, name='Options2'),
    path("history", views.history, name='history'),
    path("geography", views.geography, name='geography'),
    path("maths", views.maths, name='maths'),
    path("Phy", views.Phy, name='Phy')
    
]