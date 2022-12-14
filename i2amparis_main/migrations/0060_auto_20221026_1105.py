# Generated by Django 2.2.5 on 2022-10-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i2amparis_main', '0059_historicaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='dataset_django_model',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dataset_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dataset_provider',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='dataset_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodelgeoguides',
            name='guide_from',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodelgeoguides',
            name='guide_to',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodelgeoguides',
            name='value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodelgeoguides',
            name='workspace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltimestepguides',
            name='guide_from',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltimestepguides',
            name='guide_to',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltimestepguides',
            name='value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltimestepguides',
            name='workspace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltypeguides',
            name='guide_from',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltypeguides',
            name='guide_to',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltypeguides',
            name='value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetmodeltypeguides',
            name='workspace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetondemandvariableharmonisation',
            name='io_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetvariableharmonisationguides',
            name='guide_from',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetvariableharmonisationguides',
            name='guide_to',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetvariableharmonisationguides',
            name='value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datasetvariableharmonisationguides',
            name='workspace',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datavariablesharmonisation',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datavariablesharmonisation',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='datavariablesharmonisation',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='euharmdata',
            name='io_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='harmdatanew',
            name='io_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='harmonisation_variables',
            name='var_category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='harmonisation_variables',
            name='var_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='harmonisation_variables',
            name='var_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='projectmodels',
            name='project',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='regionsres',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='rrfpolicy',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='rrfpolicy',
            name='first_classification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='rrfpolicy',
            name='rff_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='rrfpolicy',
            name='second_classification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='scenariosres',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='unitsres',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='variable',
            name='var_category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='variable',
            name='var_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='variable',
            name='var_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='variable',
            name='var_unit',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='variable',
            name='variable_table_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='variablesres',
            name='agg_func',
            field=models.CharField(default='', max_length=100),
        ),
    ]
