# Generated by Django 4.2.1 on 2023-11-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='imagem',
            field=models.FileField(default=None, null=True, upload_to='images'),
        ),
    ]