# Generated by Django 4.1.5 on 2023-02-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scaapp', '0003_careeradvice_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
