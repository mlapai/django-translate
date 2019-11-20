from rest_framework import viewsets
from .models import Language, TranslateOption
from .serializers import LanguageSerializer, TranslateOptionSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class TranslateOptionView(viewsets.ModelViewSet):
    queryset = TranslateOption.objects.all()
    serializer_class = TranslateOptionSerializer
