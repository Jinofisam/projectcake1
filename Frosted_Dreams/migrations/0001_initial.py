# Generated by Django 5.0.7 on 2024-12-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cakeorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField()),
                ('customization', models.TextField(blank=True)),
                ('delivery_date', models.DateField()),
                ('cake_name', models.CharField(default='Cake', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=1200, max_digits=10)),
            ],
        ),
    ]
