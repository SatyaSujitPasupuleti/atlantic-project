# Generated by Django 3.2.3 on 2021-05-17 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionsproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customerorder', to='subscriptionsproject.customer')),
            ],
        ),
    ]
