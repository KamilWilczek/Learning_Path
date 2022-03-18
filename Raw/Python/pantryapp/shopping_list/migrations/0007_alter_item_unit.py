# Generated by Django 4.0.3 on 2022-03-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0006_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(blank=True, choices=[('pcs', 'pcs'), ('pkgs', 'pkgs'), ('kg', 'kg'), ('g', 'g'), ('l', 'l'), ('ml', 'ml')], max_length=20, null=True),
        ),
    ]
