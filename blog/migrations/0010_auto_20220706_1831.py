# Generated by Django 3.2 on 2022-07-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_image_post_story_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=50),
        ),
    ]