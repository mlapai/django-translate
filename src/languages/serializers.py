from rest_framework import serializers
from .models import Language, TranslateOption


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name')

class TranslateOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslateOption
        fields = (
            'id',
            'from_language',
            'to_language',
            'essential_price_per_word',
            'professional_price_per_word',
            'premium_price_per_word',
            'rush_price_percentage'
        )
