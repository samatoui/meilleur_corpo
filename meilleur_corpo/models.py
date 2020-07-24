from django.db import models, connection

class BulkManager(models.Manager):
    def batch_insert( self, *instances):
        pass

class EstateAdverts(models.Model):
    class Meta:
        db_table = 'estate_adverts'
        ordering = ['id']
        verbose_name = 'EstateAdvert'
        verbose_name_plural = 'EstateAdverts'

    COLLECTIVE, INDIVIDUAL = (
        'COLLECTIVE',
        'INDIVIDUAL',
    )

    HEATING_MODE_CHOICES = (
        (COLLECTIVE, 'Collective'),
        (INDIVIDUAL, 'Individual'),
    )

    id = models.AutoField(primary_key=True)
    ad_urls = models.CharField(max_length=255, null=True, blank=True)
    property_type = models.CharField(max_length=60, blank=True, null=True)
    dept_code = models.CharField(max_length=3, db_index=True, null=True)
    zip_code = models.CharField(max_length=10, db_index=True, null=True)
    city = models.CharField(max_length=120, db_index=True, null=True)
    insee_code = models.CharField(max_length=20, null=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    blur_radius = models.IntegerField(null=True)
    marketing_type = models.CharField(max_length=60, null=True)
    price = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    description = models.TextField(blank=True, null=True)
    surface = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    condominium_expenses = models.DecimalField(blank=True, null=True, db_index=True, max_digits=20, decimal_places=10)
    caretaker = models.CharField(max_length=120, blank=True, null=True)
    heating_mode = models.CharField(max_length=12, blank=True, null=True, db_index=True, choices=HEATING_MODE_CHOICES)
    water_heating_mode = models.CharField(max_length=60, blank=True, null=True)
    elevator = models.BooleanField(default=False, null=True, db_index=True)
    floor = models.IntegerField(blank=True, null=True, db_index=True)
    floor_count = models.DecimalField(blank=True, null=True, db_index=True, max_digits=20, decimal_places=10)
    lot_count = models.DecimalField(blank=True, null=True, db_index=True, max_digits=20, decimal_places=10)
    construction_year = models.IntegerField(blank=True, null=True)
    building_type = models.CharField(max_length=60, blank=True, null=True)
    parking = models.BooleanField(default=False, null=True)
    parking_count = models.IntegerField(blank=True, null=True, db_index=True)
    terrace = models.BooleanField(default=False, null=True)
    terrace_surface = models.DecimalField(blank=True, null=True, max_digits=20, decimal_places=10)
    swimming_pool = models.CharField(max_length=60, blank=True, null=True)
    garden = models.BooleanField(default=False, null=True)
    standing = models.BooleanField(default=False, null=True)
    new_build = models.BooleanField(default=False, null=True)
    corner_building = models.BooleanField(default=False, null=True)
    publication_start_date = models.DateTimeField(null=True,blank=True)
    dealer_name = models.CharField(max_length=60, blank=True, null=True)
    dealer_type = models.CharField(max_length=60, blank=True, null=True)
    reference_number = models.CharField(max_length=60, blank=True, null=True)
    energy_classification = models.CharField(max_length=60, blank=True, null=True)

    objects = models.Manager()
    bulk = BulkManager()

    def __str__(self):
        return str(self.id or '')
