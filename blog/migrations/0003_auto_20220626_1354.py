# Generated by Django 3.2 on 2022-06-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220625_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
