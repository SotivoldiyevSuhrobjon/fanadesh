# Generated by Django 4.1.7 on 2023-02-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanadesh_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
