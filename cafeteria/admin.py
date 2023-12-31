from django.contrib import admin
from .models import Cafeteria, FoodJournalEntry, FoodJournalImage


admin.site.register(Cafeteria)

class FoodJournalImageInline(admin.TabularInline):
    model = FoodJournalImage
    extra = 1  # Number of extra blank forms

class FoodJournalEntryAdmin(admin.ModelAdmin):
    inlines = [FoodJournalImageInline,]

admin.site.register(FoodJournalEntry, FoodJournalEntryAdmin)
