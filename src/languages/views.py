from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Language, TranslateOption
from .serializers import LanguageSerializer, TranslateOptionSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAdminUser]

class TranslateOptionView(viewsets.ModelViewSet):
    queryset = TranslateOption.objects.all()
    serializer_class = TranslateOptionSerializer
    permission_classes = [IsAdminUser]
