from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Subject, Quote
from .serializers import SubjectSerializer, QuoteSerializer


class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser]

class QuoteView(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
