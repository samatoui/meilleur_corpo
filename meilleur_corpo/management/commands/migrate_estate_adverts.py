# -*- coding: utf-8 -*-

import csv

from django.core.management.base import BaseCommand, CommandError
from os import path

from meilleur_corpo.models import EstateAdverts

class Command(BaseCommand):
    help='Migrate Real Estate Adverts'

    def add_arguments(self, parser):
        parser.add_argument('path', help= 'Path of csv file to migrate')

    def handle(self, *args, **options):
        if not path.exists(options['path']):
            raise CommandError('File "%s" does not exist' % options['path'])

        with open(options['path'], newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for id, row in enumerate(reader, start=1):
                EstateAdvert = EstateAdverts(
                    id=id,
                    ad_urls=row.get('AD_URLS') or None,
                    property_type=row.get('PROPERTY_TYPE') or None,
                    dept_code=row.get('DEPT_CODE') or None,
                    zip_code=row.get('ZIP_CODE') or None,
                    city=row.get('CITY') or None,
                    insee_code=row.get('INSEE_CODE') or None,
                    latitude=row.get('LATITUDE') or None,
                    longitude=row.get('LONGITUDE') or None,
                    blur_radius=row.get('BLUR_RADIUS') or None,
                    marketing_type=row.get('MARKETING_TYPE') or None,
                    price=row.get('PRICE') or 0,
                    description=row.get('DESCRIPTION') or None,
                    surface=row.get('SURFACE') if row.get('SURFACE').isnumeric() else None,
                    condominium_expenses=row.get('CONDOMINIUM_EXPENSES') or 0,
                    caretaker=row.get('CARETAKER') or None,
                    heating_mode=row.get('HEATING_MODE') or None,
                    water_heating_mode=row.get('WATER_HEATING_MODE') or None,
                    elevator=row.get('ELEVATOR') or False,
                    floor=row.get('FLOOR') or None,
                    floor_count=row.get('FLOOR_COUNT') or None,
                    lot_count=row.get('LOT_COUNT') or None,
                    construction_year=row.get('CONSTRUCTION_YEAR') or None,
                    building_type=row.get('BUILDING_TYPE') or None,
                    parking=row.get('PARKING') or None,
                    parking_count=row.get('PARKING_COUNT') or None,
                    terrace=row.get('TERRACE') or None,
                    terrace_surface=row.get('TERRACE_SURFACE') or None,
                    swimming_pool=row.get('SWIMMING_POOL') or None,
                    garden=row.get('GARDEN') or None,
                    standing=row.get('STANDING') or None,
                    new_build=row.get('NEW_BUILD') or None,
                    corner_building=row.get('CORNER_BUILDING') or None,
                    publication_start_date=row.get('PUBLICATION_START_DATE') or None,
                    dealer_name=row.get('DEALER_NAME') or None,
                    dealer_type=row.get('DEALER_TYPE') or None,
                    reference_number=row.get('REFERENCE_NUMBER') or None,
                    energy_classification=row.get('ENERGY_CLASSIFICATION') or None,
                )
                EstateAdvert.save()
