# Generated by Django 2.2.3 on 2019-08-04 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190720_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='class_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.ClassRegistration'),
        ),
    ]
