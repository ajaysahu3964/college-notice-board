# Generated by Django 3.0.8 on 2020-07-31 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegenotice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('msg', models.CharField(max_length=1000)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collegenotice.branch')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
