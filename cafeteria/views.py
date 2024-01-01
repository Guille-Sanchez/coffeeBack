# views.py
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Cafeteria, FoodJournalEntry
from .serializers import CafeteriaSerializer, FoodJournalEntrySerializer

class CafeteriaViewset(viewsets.ModelViewSet):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer

    def list(self, request, *args, **kwargs):
        cafeteria_name = request.query_params.get('name', None)

        if cafeteria_name:
            queryset = self.get_queryset().order_by('id')
            serializer = FoodJournalEntrySerializer(queryset, many=True, context={'request': request})
            return Response(serializer.data)

        queryset = self.get_queryset().order_by('id')
        serializer = CafeteriaSerializer(queryset, many=True, context={'request': request})
        result = {item['name']: item for item in serializer.data}
        for cafe in result.values():
            del cafe['name']
        return Response(result)


    def get_queryset(self):
        cafeteria_name = self.request.query_params.get('name', None)
        if cafeteria_name:
            cafeteria = get_object_or_404(Cafeteria, name=cafeteria_name)
            return FoodJournalEntry.objects.filter(cafeteria=cafeteria)
        return super().get_queryset()
