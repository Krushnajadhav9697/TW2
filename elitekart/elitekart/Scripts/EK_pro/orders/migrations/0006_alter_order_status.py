# Generated by Django 5.1.4 on 2024-12-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status_remove_orderproduct_variation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('New', 'New'), ('Accepted', 'Accepted')], default='New', max_length=10),
        ),
    ]
