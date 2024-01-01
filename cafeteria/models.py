from django.db import models
from django.dispatch import receiver
import os
from django.db.models.signals import pre_save, post_save
import logging

logger = logging.getLogger(__name__)
def delete_old_file(old_file_path):
    if old_file_path and os.path.isfile(old_file_path):
        try:
            os.remove(old_file_path)
            logger.info(f"Successfully deleted old image at {old_file_path}")
        except Exception as e:
            logger.error(f"Error deleting file {old_file_path}: {e}")


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
    
    def set_current_image_path(self):
        if self.cafeteria_image:
            self._current_image_path = self.cafeteria_image.path
        else:
            self._current_image_path = None


@receiver(pre_save, sender=Cafeteria)
def set_old_image_path(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            instance._current_image_path = old_instance.cafeteria_image.path
        except sender.DoesNotExist:
            pass

@receiver(post_save, sender=Cafeteria)
def delete_old_images(sender, instance, **kwargs):
    # Handle cafeteria_image
    if hasattr(instance, '_old_cafeteria_image_path'):
        new_cafeteria_image_path = instance.cafeteria_image.path if instance.cafeteria_image else None
        if instance._old_cafeteria_image_path != new_cafeteria_image_path:
            delete_old_file(instance._old_cafeteria_image_path)

    # Handle menu image
    if hasattr(instance, '_old_menu_image_path'):
        new_menu_image_path = instance.menu.path if instance.menu else None
        if instance._old_menu_image_path != new_menu_image_path:
            delete_old_file(instance._old_menu_image_path)


@receiver(pre_save, sender=Cafeteria)
def set_old_image_path_cafeteria(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            instance._old_cafeteria_image_path = old_instance.cafeteria_image.path if old_instance.cafeteria_image else None
            instance._old_menu_image_path = old_instance.menu.path if old_instance.menu else None
        except sender.DoesNotExist:
            pass

@receiver(post_save, sender=Cafeteria)
def delete_old_image_cafeteria(sender, instance, **kwargs):
    if hasattr(instance, '_old_cafeteria_image_path'):
        new_image_path = instance.cafeteria_image.path if instance.cafeteria_image else None
        delete_old_file(instance._old_cafeteria_image_path) if instance._old_cafeteria_image_path != new_image_path else None
    
    if hasattr(instance, '_old_menu_image_path'):
        new_menu_path = instance.menu.path if instance.menu else None
        delete_old_file(instance._old_menu_image_path) if instance._old_menu_image_path != new_menu_path else None

    
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


@receiver(pre_save, sender=FoodJournalImage)
def set_old_image_path_journal(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            instance._old_image_path = old_instance.image.path if old_instance.image else None
        except sender.DoesNotExist:
            pass

@receiver(post_save, sender=FoodJournalImage)
def delete_old_image_journal(sender, instance, **kwargs):
    if hasattr(instance, '_old_image_path'):
        new_image_path = instance.image.path if instance.image else None
        delete_old_file(instance._old_image_path) if instance._old_image_path != new_image_path else None