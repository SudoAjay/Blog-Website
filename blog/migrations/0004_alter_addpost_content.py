# Generated by Django 4.2 on 2023-04-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_addpost_author_alter_addpost_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
