# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Cafeteria, FoodJournalEntry
from .serializers import CafeteriaSerializer, FoodJournalEntrySerializer

class CafeteriaViewset(viewsets.ModelViewSet):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        cafeteria_name = self.request.query_params.get('name', None)

        if cafeteria_name:
            cafeteria = get_object_or_404(Cafeteria, name=cafeteria_name)
            return FoodJournalEntry.objects.filter(cafeteria=cafeteria)

        return queryset

    def get_serializer_class(self):
        if 'name' in self.request.query_params:
            return FoodJournalEntrySerializer
        return super().get_serializer_class()
