# Generated by Django 4.2.13 on 2024-07-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]