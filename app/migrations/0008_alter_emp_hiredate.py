# Generated by Django 4.2.7 on 2023-12-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_dept_adr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='Hiredate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
