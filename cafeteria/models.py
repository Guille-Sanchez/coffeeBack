from django.db import models
from datetime import date


# Create your models here.
class Cafeteria(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    maps = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    menu = models.ImageField(upload_to='menu', blank=True, null=True)
    cafeteria_image = models.ImageField(upload_to='cafeterias', blank=True, null=True)

    def __str__(self):
        return self.name
    
class FoodJournalEntry(models.Model):
    cafeteria = models.ForeignKey(Cafeteria, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        date_str = self.date.strftime('%Y-%m-%d')
        return f'{self.cafeteria.name} - {date_str}'
    
class FoodJournalImage(models.Model):
    journal_entry = models.ForeignKey(FoodJournalEntry, related_name='coffee_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cafeteria_images')

    def __str__(self):
        return f"Image for {self.journal_entry}"