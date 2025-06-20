# Generated by Django 5.2.1 on 2025-05-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.CharField(blank=True, max_length=7, null=True)),
                ('total_served', models.IntegerField(blank=True, null=True)),
                ('total_possible', models.IntegerField(blank=True, null=True)),
                ('difference_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
