# Generated by Django 3.1.3 on 2021-05-31 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('igo', '0024_auto_20210531_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment1',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igo.review1'),
        ),
        migrations.AlterField(
            model_name='comment2',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igo.review2'),
        ),
        migrations.AlterField(
            model_name='comment3',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igo.review3'),
        ),
        migrations.AlterField(
            model_name='comment4',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igo.review4'),
        ),
        migrations.AlterField(
            model_name='comment5',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='igo.review5'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review1',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review2',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review3',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review4',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review4', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review5',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_review5', to=settings.AUTH_USER_MODEL),
        ),
    ]
