# yourapp/management/commands/import_cities.py
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from src.accounts.models import City

# print("ROW: ", row)


class Command(BaseCommand):
    help = 'Import cities from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                row_id = row.get('\ufeffid', row['id'])

                # Convert 'modification_date' to the correct format
                modification_date = datetime.strptime(
                    row['modification_date'], '%m/%d/%Y').strftime('%Y-%m-%d')

                city, created = City.objects.get_or_create(
                    id=row_id,
                    defaults={
                        'name': row['name'],
                        'asciiname': row['asciiname'],
                        'alternatenames': row['alternatenames'],
                        'latitude': float(row['latitude']),
                        'longitude': float(row['longitude']),
                        'country': row['country'],
                        'population': int(row['population']),
                        'timezone': row['timezone'],
                        'modification_date': modification_date,
                    }
                )

                if not created:
                    # City already exists, update other fields if needed
                    city.name = row['name']
                    city.asciiname = row['asciiname']
                    city.alternatenames = row['alternatenames']
                    city.latitude = float(row['latitude'])
                    city.longitude = float(row['longitude'])
                    city.country = row['country']
                    city.population = int(row['population'])
                    city.timezone = row['timezone']
                    city.modification_date = modification_date  # Update to the correct format
                    city.save()

        self.stdout.write(self.style.SUCCESS('Cities imported successfully.'))
