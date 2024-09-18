from django.db import models

# Create your models here.
class Tour (models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    price = models.IntegerField()
    number_of_days = models.IntegerField()

    def __str__(self):
        return (f"travel id {self.id} origin {self.origin_country} to {self.destination_country} costs Rs{self.price} for {self.number_of_days}days")
    
