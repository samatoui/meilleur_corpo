# -*- coding: utf-8 -*-

import csv

from django.db import connection
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
        data = []
        EstateAdverts.objects.all().delete()

        with open(options['path'], newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for id, row in enumerate(reader, start=1):
                data.append(
                    EstateAdverts(
                        id=id,
                        dept_code=row.get('DEPT_CODE') or None,
                        zip_code=row.get('ZIP_CODE') or None,
                        city=row.get('CITY') or None,
                        condominium_expenses=row.get('CONDOMINIUM_EXPENSES') or 0,
                        heating_mode=row.get('HEATING_MODE') or None,
                        elevator=row.get('ELEVATOR') or False,
                    )
                )

                if id % 100:
                    EstateAdverts.objects.bulk_create(data)
                    data=[]
