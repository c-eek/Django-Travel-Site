from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    place = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.name} on {self.date} at {self.time}"

# Create your models here.
