# Generated by Django 4.0.1 on 2022-05-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0005_mydata_absent_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='Absenties',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
