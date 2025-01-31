from django.db import models
from datetime import date


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(blank=False, max_length=56)
    last_name = models.CharField(blank=False, max_length=40)
    date_rented = models.DateTimeField(blank=False, auto_now_add=True)
    due_date = models.DateTimeField(blank=False)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    


class Car(models.Model):
    car_name = models.CharField(blank=False, max_length=40)
    car_type = models.CharField(blank=False, max_length=40)
    model = models.CharField(max_length=40)
    colour = models.CharField(max_length=30)
    description = models.TextField
    is_rented = models.BooleanField
    rented_by = models.ForeignKey(Person, related_name='cars_app', on_delete=models.CASCADE)
    
    
    
