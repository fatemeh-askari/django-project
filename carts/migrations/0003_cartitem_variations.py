# Generated by Django 4.2.3 on 2023-09-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation_is_active'),
        ('carts', '0002_rename_card_id_cart_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
