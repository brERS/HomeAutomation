# Generated by Django 4.1.7 on 2023-03-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('title_highlight', models.CharField(max_length=150)),
                ('title_finish', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubNav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('url', models.CharField(max_length=65)),
                ('icon', models.CharField(max_length=40)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubNavContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('content', models.TextField()),
                ('subcontent', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('additional_js', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
            ],
        ),
    ]
