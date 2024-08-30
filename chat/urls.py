from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat_page", views.chat_page, name="chat_page"),
    path("feedback_page", views.feedback_page, name="feedback_page"),

    path("chat", views.chat, name="chat"),
    path("feedback", views.feedback, name="feedback"),
]
