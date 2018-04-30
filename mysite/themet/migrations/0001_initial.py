# Generated by Django 2.0 on 2018-04-30 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300)),
                ('teaserText', models.CharField(max_length=300)),
                ('url', models.CharField(max_length=300)),
                ('image', models.URLField(max_length=300)),
                ('regularImage', models.CharField(max_length=300)),
                ('largeImage', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('accessionNumber', models.CharField(max_length=20)),
                ('galleryInformation', models.CharField(max_length=300)),
            ],
        ),
    ]