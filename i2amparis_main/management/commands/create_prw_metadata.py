from django.core.management.base import BaseCommand, CommandError
from i2amparis_main.models import ResultsComp, PRWMetaData, PRWEUMetaData
from django.apps import apps


# Documentation

# create_prw_metadata i2amparis_main resultscomp prwmetadata : for creating metadata for PR Global Workspace
# create_prw_metadata i2amparis_main wwheuresultscomp prweumetadata : for creating metadata for PR EU Workspace

class Command(BaseCommand):
    help = 'Created metadata for I2AM PARIS Workspaces'

    def add_arguments(self, parser):
        parser.add_argument('app_name', nargs='+', type=str,
                            help='application_name')
        parser.add_argument('dataset_name', nargs='+', type=str,
                            help='dataset_name')
        parser.add_argument('metadata_table', nargs='+', type=str,
                            help='metadata_table')

    def handle(self, *args, **options):
        app_name = options['app_name'][0]
        dataset = options['dataset_name'][0]
        metadata_table = options['metadata_table'][0]

        metadata = apps.get_model(app_name, metadata_table)
        self.stdout.write('Current Metadata Length: {}\nDeleting...'.format(len(metadata.objects.all())))
        metadata.objects.all().delete()

        data = apps.get_model(app_name, dataset).objects.values('model__name', 'scenario__name', 'region__name',
                                                                'variable__name').distinct()
        md_length = len(data)
        count = 0
        self.stdout.write('Passing all metadata of {}...'.format(dataset))

        for d in data:
            try:
                md_obj = metadata(model_name=d['model__name'], scenario_name=d['scenario__name'],
                                     region_name=d['region__name'], variable_name=d['variable__name'])
                md_obj.save()
                count = count + 1
                print(f'Complete:{round((100*count)/md_length,2)}%')
            except:
                raise CommandError('{} out of {} passed'.format(count, md_length))
        self.stdout.write(
            'Successfully created metadata for dataset {} and placed in {}!'.format(dataset, metadata_table))
