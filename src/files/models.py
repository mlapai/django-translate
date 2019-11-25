from django.db import models
from src.quotes.models import Quote


class MyFile(models.Model):
    file = models.FileField(blank=False, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
