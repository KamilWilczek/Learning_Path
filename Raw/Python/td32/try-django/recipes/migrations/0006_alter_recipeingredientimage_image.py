# Generated by Django 4.0.3 on 2022-04-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipeingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
    ]
