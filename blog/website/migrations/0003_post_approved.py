# Generated by Django 3.1.5 on 2021-01-27 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
