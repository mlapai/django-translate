from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TranslateOption(models.Model):
    from_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='from_language')
    to_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='to_language')
    essential_price_per_word = models.DecimalField(max_digits=6, decimal_places=2)
    professional_price_per_word = models.DecimalField(max_digits=6, decimal_places=2)
    premium_price_per_word = models.DecimalField(max_digits=6, decimal_places=2)
    rush_price_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('from_language', 'to_language')
