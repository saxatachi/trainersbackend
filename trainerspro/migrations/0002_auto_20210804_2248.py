# Generated by Django 3.2 on 2021-08-04 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=100)),
                ('client_email', models.EmailField(default='', max_length=254)),
                ('client_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('completed', models.BooleanField(default=False)),
                ('events', models.ManyToManyField(to='trainerspro.Event')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainerspro.package')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]