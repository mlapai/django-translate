from rest_framework import serializers

from .models import Language, TranslateOption


class LanguageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)

    class Meta:
        model = Language
        fields = ('id', 'name')

class TranslateOptionSerializer(serializers.ModelSerializer):
    essential_price_per_word = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0.01)
    professional_price_per_word = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0.01)
    premium_price_per_word = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=0.01)

    def validate(self, data):
        if data['from_language'] == data['to_language']:
            raise serializers.ValidationError("Language cannot be translated to itself.")
        return data

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
