from django.db import models

# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(default=0)
    bookingdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
