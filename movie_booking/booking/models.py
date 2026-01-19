from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=50) 
    movie_title = models.CharField(max_length=200)
    show_time = models.CharField(max_length=20)
    seats = models.IntegerField()
    base_price = models.FloatField()  
    service_fee = models.FloatField() 
    tax = models.FloatField()  
    total_price = models.FloatField()  
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} - {self.user.username}"
