# Generated by Django 4.0.3 on 2022-04-20 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipeingredientimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredientimage',
            name='extracted',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
