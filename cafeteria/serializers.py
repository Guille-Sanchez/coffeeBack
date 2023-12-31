from rest_framework import serializers
from .models import Cafeteria, FoodJournalEntry

class CafeteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = '__all__'

class FoodJournalEntrySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = FoodJournalEntry
        exclude = ('cafeteria',)

    def get_images(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(image.image.url) for image in obj.coffee_images.all()]