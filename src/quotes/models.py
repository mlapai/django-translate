from django.db import models
from src.languages.models import TranslateOption

class Subject(models.Model):
    name = models.CharField(max_length=50)
    additional_price_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    translate_option_id = models.ForeignKey(TranslateOption, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_word_count = models.PositiveIntegerField()
    service_tier = models.PositiveSmallIntegerField()
    in_rush = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
