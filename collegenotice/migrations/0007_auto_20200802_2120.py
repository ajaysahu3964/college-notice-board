# Generated by Django 3.0.8 on 2020-08-02 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegenotice', '0006_auto_20200802_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hod',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='collegenotice.branch'),
        ),
    ]
