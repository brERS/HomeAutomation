# Generated by Django 4.1.7 on 2023-03-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0003_remove_subnav_additional_js_remove_subnav_is_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnavcontent',
            name='function_button',
            field=models.CharField(blank=True, max_length=65),
        ),
    ]