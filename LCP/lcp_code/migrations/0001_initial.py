# Generated by Django 4.0.6 on 2022-07-27 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=250, verbose_name='Nombre Comprador')),
            ],
        ),
        migrations.CreateModel(
            name='LcpType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lcp_type', models.CharField(max_length=50, verbose_name='Tipo de proyecto Inversion')),
            ],
        ),
        migrations.CreateModel(
            name='StakeHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stake_holder_name', models.CharField(max_length=250, verbose_name='Nombre del cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Lcp_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(auto_now_add=True, verbose_name='Creacion proyecto')),
                ('lcp_code', models.CharField(max_length=50, verbose_name='Codigo completo ej.LCP-210210-01')),
                ('lcp_name', models.CharField(max_length=250, verbose_name='Nombre del proyecto')),
                ('lcp_description', models.CharField(max_length=250, verbose_name='Descripcion del proyecto')),
                ('lcp_status', models.BinaryField(verbose_name='0: open, 1:close')),
                ('project_type', models.CharField(max_length=100, verbose_name='Tipo de proyecto')),
                ('lcp_options', models.JSONField(verbose_name='Opciones de estado')),
                ('buyer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcp_code.buyer', verbose_name='Nombre del comprador')),
                ('lcp_stake_holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcp_code.stakeholder', verbose_name='Cliente interno')),
                ('lcp_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lcp_code.lcptype', verbose_name='Capex/Expense/Miscelaneous')),
            ],
        ),
    ]
