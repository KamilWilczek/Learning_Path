# Generated by Django 4.0.3 on 2022-03-24 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]
