# Generated by Django 3.0.7 on 2023-06-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salebilldetails',
            name='cess',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='cgst',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='eway',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='igst',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='po',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='sgst',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='tcs',
        ),
        migrations.RemoveField(
            model_name='salebilldetails',
            name='veh',
        ),
        migrations.AddField(
            model_name='salebilldetails',
            name='tracking_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
