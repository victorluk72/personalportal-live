# Generated by Django 3.0.2 on 2020-03-23 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appContacts', '0004_countrycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscontact',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appContacts.CountryCode'),
        ),
    ]
