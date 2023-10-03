# Generated by Django 4.2.1 on 2023-10-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_choice_choice_text_alter_question_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor da doação')),
                ('confirmacao', models.BooleanField(default=False, verbose_name='Pagamento confirmado?')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço Completo')),
            ],
        ),
    ]