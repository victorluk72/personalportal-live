# Generated by Django 3.0.2 on 2020-02-29 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appContacts', '0002_auto_20200228_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesscontact',
            name='businessType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appContacts.BusinesType'),
        ),
        migrations.AlterField(
            model_name='childcontact',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appContacts.PersonalContact'),
        ),
    ]
