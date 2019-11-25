from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('languages', '0001_squashed_0002_auto_20191125_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
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
                ('total_word_count', models.PositiveIntegerField()),
                ('service_tier', models.PositiveSmallIntegerField()),
                ('in_rush', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
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
                ('additional_price_percentage', models.DecimalField(decimal_places=1, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='quote',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Subject'),
        ),
        migrations.AddField(
            model_name='quote',
            name='translate_option_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='languages.TranslateOption'
            ),
        ),
    ]
