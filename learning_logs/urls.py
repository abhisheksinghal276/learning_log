"""Defines URL patterns for learning_logs."""

from django.urls import path, include
from . import views 

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Topic page
    path('topics/', views.topics, name='topics'),

    # Individual Topic Page
    path('topics/<int:topic_id>', views.topic, name='topic'),

    # New Topic page
    path('new_topic/', views.new_topic, name='new_topic'),

    # New Entry for topic (new or old)
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),

    # Edit an old entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
