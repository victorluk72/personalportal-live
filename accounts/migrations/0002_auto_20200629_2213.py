# Generated by Django 3.0.2 on 2020-06-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_b_pagination',
            field=models.IntegerField(default=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_p_pagination',
            field=models.IntegerField(default=15, null=True),
        ),
    ]
