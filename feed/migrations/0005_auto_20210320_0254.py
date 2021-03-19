# Generated by Django 3.1.6 on 2021-03-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20210320_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='quantity',
            field=models.CharField(choices=[('less than 15', 'LESS THAN 15'), ('less than 20', 'LESS THAN 20'), ('less than 30', 'LESS THAN 30'), ('less than 50', 'LESS THAN 50'), ('more than 50', 'MORE THAN 50')], default='less than 15', max_length=15),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='address',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='meal',
            field=models.CharField(choices=[('breakfast', 'BREAKFAST'), ('dinner', 'DINNER'), ('lunch', 'LUNCH')], default='dinner', max_length=15),
        ),
    ]