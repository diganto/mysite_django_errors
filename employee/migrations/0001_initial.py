# Generated by Django 3.1.3 on 2020-11-28 18:12

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Muser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=24)),
                ('ranking', models.FloatField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=employee.models.Muser.upload_dir)),
                ('resume', models.ImageField(blank=True, null=True, upload_to=employee.models.Muser.upload_file)),
            ],
        ),
    ]