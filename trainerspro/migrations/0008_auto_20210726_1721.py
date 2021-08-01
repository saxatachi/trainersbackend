# Generated by Django 3.2 on 2021-07-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0007_auto_20210726_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='stripe_id',
            new_name='stripe_product_id',
        ),
        migrations.AddField(
            model_name='package',
            name='stripe_product_price',
            field=models.CharField(default='', max_length=50),
        ),
    ]