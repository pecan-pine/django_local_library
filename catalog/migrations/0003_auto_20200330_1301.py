# Generated by Django 3.0.4 on 2020-03-30 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='lang',
            field=models.CharField(max_length=100),
        ),
    ]
