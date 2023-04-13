from django.db import models
from django.urls import reverse

# Create your models here.

class Play_Date(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('play_detail', kwargs={'pk': self.id})

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    image = models.TextField()
    temperment = models.TextField()
    play = models.ManyToManyField(Play_Date)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('details', kwargs={'cat_id': self.id})


VISITS = (
    ('V', 'Vaccine'),
    ('C', 'Checkup'),
    ('G', 'Grooming'),
)

class Appointment(models.Model):
    date = models.DateField('Visit Date')
    visit = models.CharField(choices=VISITS, default=VISITS[0][0])

    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return f'{self.get_visit_display()} on {self.date}'