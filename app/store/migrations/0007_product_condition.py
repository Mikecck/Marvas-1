# Generated by Django 2.2 on 2022-01-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220121_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Condition',
            field=models.BooleanField(default=False, null=True),
        ),
    ]