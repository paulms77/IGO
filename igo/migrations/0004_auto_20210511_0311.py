# Generated by Django 3.1.3 on 2021-05-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igo', '0003_auto_20210511_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('shop_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='%Y/%m/%d')),
                ('contents', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Reivew',
        ),
    ]