from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=200)

    # Functions
    def __str__(self):
        """Return a string representation of the model"""
        return self.name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    # Functions
    def __str__(self):
        """Return a string representation of the model"""
        return self.name
