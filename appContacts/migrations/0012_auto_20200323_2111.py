# Generated by Django 3.0.2 on 2020-03-24 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContacts', '0011_auto_20200323_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscontact',
            name='country',
            field=models.CharField(blank=True, choices=[('CA', 'Canada'), ('US', 'Unated States'), ('UA', 'Ukraine'), ('RU', 'Russia'), ('DE', 'Germany'), ('FR', 'France'), ('PT', 'Portugal')], max_length=50),
        ),
    ]