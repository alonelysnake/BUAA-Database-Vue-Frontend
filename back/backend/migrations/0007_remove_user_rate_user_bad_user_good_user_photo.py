# Generated by Django 4.1.3 on 2022-12-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_comment_content_alter_news_target_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='rate',
        ),
        migrations.AddField(
            model_name='user',
            name='bad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='good',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.CharField(default='', max_length=2560),
        ),
    ]