# Generated by Django 3.1.3 on 2021-06-18 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('igo', '0027_auto_20210601_0402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='Review',
        ),
        migrations.CreateModel(
            name='Review6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('shop_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
