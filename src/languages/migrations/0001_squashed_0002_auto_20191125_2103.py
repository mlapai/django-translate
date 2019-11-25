from django.db import migrations, models
import django.db.models.deletion

from django.conf.global_settings import LANGUAGES
from ..models import Language

def seed_languages(app, schema_editor):
    for language in LANGUAGES:
        if 2 > len(language):
            continue

        new_language = Language(name=language[1])
        new_language.save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TranslateOption',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'essential_price_per_word',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=6
                    )
                ),
                ('professional_price_per_word', models.DecimalField(decimal_places=2, max_digits=6)),
                ('premium_price_per_word', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rush_price_percentage', models.DecimalField(decimal_places=1, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'from_language',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='from_language',
                        to='languages.Language'
                    )
                ),
                (
                    'to_language',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='to_language',
                        to='languages.Language'
                    )
                ),
            ],
        ),
        migrations.RunPython(seed_languages),
        migrations.AlterUniqueTogether(
            name='translateoption',
            unique_together={('from_language', 'to_language')},
        ),
    ]
