# Generated by Django 3.2.17 on 2023-02-11 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.subject'),
        ),
    ]
