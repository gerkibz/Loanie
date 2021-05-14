# Generated by Django 3.1.7 on 2021-05-09 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_loantypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='gurrantor_1',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='gurrantor_1_ID',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='gurrantor_2',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loan',
            name='gurrantor_2_ID',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]