from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.title} : str{(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests=models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    booking_date= models.DateTimeField()
    menu_item=models.ForeignKey(Menu, on_delete=models.CASCADE, null=True) 

