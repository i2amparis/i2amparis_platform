# Generated by Django 2.2.5 on 2022-11-08 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i2amparis_main', '0060_auto_20221026_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='COVIDMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='', max_length=100)),
                ('scenario_name', models.CharField(default='', max_length=100)),
                ('region_name', models.CharField(default='', max_length=100)),
                ('variable_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='COVIDResultsComp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('value', models.FloatField()),
                ('model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='i2amparis_main.DataVariablesModels')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i2amparis_main.RegionsRes')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i2amparis_main.ScenariosRes')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i2amparis_main.UnitsRes')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i2amparis_main.VariablesRes')),
            ],
        ),
    ]
