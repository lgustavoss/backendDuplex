# Generated by Django 4.2.6 on 2023-10-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0002_alter_pessoa_cnpj_cpf_alter_pessoa_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cliente',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='fornecedor',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='transportadora',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='vendedor',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
