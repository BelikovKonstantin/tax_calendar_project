# Generated by Django 2.2.19 on 2021-05-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulator',
            name='slug',
            field=models.SlugField(default='a'),
        ),
    ]