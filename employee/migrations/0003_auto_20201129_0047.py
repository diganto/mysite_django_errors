# Generated by Django 3.1.3 on 2020-11-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_muser_emp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='muser',
            name='id',
        ),
        migrations.AddField(
            model_name='muser',
            name='emp_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]