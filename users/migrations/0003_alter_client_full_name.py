# Generated by Django 5.0.6 on 2024-05-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_author_last_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='full_name',
            field=models.CharField(max_length=256),
        ),
    ]
