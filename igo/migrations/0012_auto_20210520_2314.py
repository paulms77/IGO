# Generated by Django 3.1.3 on 2021-05-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igo', '0011_auto_20210513_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]