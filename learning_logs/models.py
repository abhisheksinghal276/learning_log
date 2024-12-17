import django.db
from django.db import models

# Importing required modules for connecting data to users
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    # Attributes
    """A Topic user is learning about"""
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Functions
    def __str__(self):
        """Return a string representation of the model"""
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return a string representation of model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."

        return self.text

