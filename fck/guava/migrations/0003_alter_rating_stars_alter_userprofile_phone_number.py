# Generated by Django 5.1.3 on 2024-12-03 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guava', '0002_alter_productphoto_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='stars',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]