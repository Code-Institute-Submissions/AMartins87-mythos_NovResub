# Generated by Django 3.2 on 2022-07-02 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_title_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='story_image',
        ),
    ]