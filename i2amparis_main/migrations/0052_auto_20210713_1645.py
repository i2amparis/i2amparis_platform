# Generated by Django 2.2.5 on 2021-07-13 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i2amparis_main', '0051_rrfpolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variablesres',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='WWHEUResultsComp',
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
