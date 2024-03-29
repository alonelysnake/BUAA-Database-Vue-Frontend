# Generated by Django 4.1.3 on 2022-12-20 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_remove_discount_user_discount_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='country',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='game',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='user',
        ),
        migrations.AlterField(
            model_name='price',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='GameDiscount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.country')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.discount')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.game')),
            ],
        ),
    ]
