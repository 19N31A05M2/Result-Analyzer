# Generated by Django 4.0.1 on 2022-04-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='Section',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]