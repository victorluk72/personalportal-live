# Generated by Django 3.0.2 on 2020-03-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContacts', '0012_auto_20200323_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscontact',
            name='country_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='personalcontact',
            name='country_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='businesscontact',
            name='country',
            field=models.CharField(blank=True, choices=[('CA', 'Canada'), ('US', 'Unated States of America'), ('UA', 'Ukraine'), ('RU', 'Russia'), ('DE', 'Germany'), ('FR', 'France'), ('PT', 'Portugal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='personalcontact',
            name='country',
            field=models.CharField(blank=True, choices=[('CA', 'Canada'), ('US', 'Unated States of America'), ('UA', 'Ukraine'), ('RU', 'Russia'), ('DE', 'Germany'), ('FR', 'France'), ('PT', 'Portugal')], default='Canada', max_length=50),
        ),
    ]
