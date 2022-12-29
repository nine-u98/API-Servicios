# Generated by Django 4.1.4 on 2022-12-24 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_alter_services_logo_alter_services_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expired_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_user_id', models.CharField(max_length=150)),
                ('penalty_fee_amount', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'expired_payment',
            },
        ),
        migrations.CreateModel(
            name='Payment_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0.0)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='services.services')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment_user',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(choices=[('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Start+'), ('PM', 'Paramount+')], default='NF', max_length=2)),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('monto', models.FloatField(default=0.0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
    ]
