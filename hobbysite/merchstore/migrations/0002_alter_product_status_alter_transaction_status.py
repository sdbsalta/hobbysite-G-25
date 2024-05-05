# Generated by Django 5.0.2 on 2024-05-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('On Sale', 'On Sale'), ('Out of Stock', 'Out of Stock')], default='Available', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('On cart', 'On cart'), ('To Pay', 'To Pay'), ('To ship', 'To Ship'), ('To receive', 'To Receive'), ('Delivered', 'Delivered')], max_length=20),
        ),
    ]
