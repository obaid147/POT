# Generated by Django 4.2.7 on 2024-05-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordertracker',
            name='purchase_order_id',
            field=models.CharField(editable=False, max_length=20, unique=True),
        ),
    ]
