from rest_framework import serializers

from .models import Subject, Quote


class SubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    additional_price_percentage = serializers.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        model = Subject
        fields = ('id', 'name', 'additional_price_percentage')

class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = (
            'id',
            'translate_option_id',
            'subject_id',
            'total_word_count',
            'service_tier',
            'in_rush',
            'price'
        )
