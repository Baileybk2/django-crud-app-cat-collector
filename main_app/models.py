from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})
    

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # second arguement means that if the user is deleted, its associated cats and data will also be deleted 

    def __str__(self):
        return self.name    
    
      # Define a method to get the URL for this particular cat instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('cat-detail', kwargs={'cat_id': self.id})
    
class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
        # first 0 references the first tuple in meals, and the second 0 references the first position in the first tuple
        )
    
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    # whenever associated or parent model is deleted(a cat) this line will automatically delete the feedings 
    
    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']



