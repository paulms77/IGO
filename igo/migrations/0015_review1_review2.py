# Generated by Django 3.1.3 on 2021-05-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igo', '0014_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('shop_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('shop_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
