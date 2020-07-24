# Generated by Django 3.0.8 on 2020-07-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstateAdverts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad_urls', models.CharField(blank=True, max_length=255, null=True)),
                ('property_type', models.CharField(blank=True, max_length=60, null=True)),
                ('dept_code', models.CharField(db_index=True, max_length=3, null=True)),
                ('zip_code', models.CharField(db_index=True, max_length=5, null=True)),
                ('city', models.CharField(db_index=True, max_length=120, null=True)),
                ('insee_code', models.CharField(max_length=20, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('blur_radius', models.IntegerField(null=True)),
                ('marketing_type', models.CharField(max_length=60, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('surface', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('condominium_expenses', models.CharField(blank=True, max_length=120, null=True)),
                ('caretaker', models.CharField(blank=True, max_length=120, null=True)),
                ('heating_mode', models.CharField(blank=True, max_length=60, null=True)),
                ('water_heating_mode', models.CharField(blank=True, max_length=60, null=True)),
                ('elevator', models.IntegerField(blank=True, db_index=True, null=True)),
                ('floor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('floor_count', models.IntegerField(blank=True, db_index=True, null=True)),
                ('lot_count', models.IntegerField(blank=True, db_index=True, null=True)),
                ('construction_year', models.IntegerField(blank=True, null=True)),
                ('building_type', models.CharField(blank=True, max_length=60, null=True)),
                ('parking', models.BooleanField(default=False, null=True)),
                ('parking_count', models.IntegerField(blank=True, db_index=True, null=True)),
                ('terrace', models.BooleanField(default=False, null=True)),
                ('terrace_surface', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('swimming_pool', models.CharField(blank=True, max_length=60, null=True)),
                ('garden', models.BooleanField(default=False, null=True)),
                ('standing', models.BooleanField(default=False, null=True)),
                ('new_build', models.BooleanField(default=False, null=True)),
                ('corner_building', models.BooleanField(default=False, null=True)),
                ('publication_start_date', models.DateTimeField(blank=True, null=True)),
                ('dealer_name', models.CharField(blank=True, max_length=60, null=True)),
                ('dealer_type', models.CharField(blank=True, max_length=60, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=60, null=True)),
                ('energy_classification', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name': 'EstateAdvert',
                'verbose_name_plural': 'EstateAdverts',
                'db_table': 'estate_adverts',
                'ordering': ['id'],
            },
        ),
    ]
