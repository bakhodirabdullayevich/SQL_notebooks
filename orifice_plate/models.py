from django.db import models

from objects.models import Meter


# Create your models here.
class OrificePlate(models.Model):
    UNITS = (
        ('kPa', 'kPa'),
        ('MPa', 'MPa'),
        ('kgf/m2', 'kgf/m2'),
        ('kgf/sm2', 'kgf/sm2'),
        ('bar', 'bar'),
    )
    INSTALLED = (
        ('O`rnatilgan', 'O`rnatilgan'),
        ('O`rnatilmagan', 'O`rnatilmagan'),
    )
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, null=True, blank=True,
                              limit_choices_to={'object_id': models.F('object_id')})
    number = models.CharField(max_length=10)
    d20 = models.DecimalField(max_digits=5, decimal_places=2)
    outer_diameter = models.DecimalField(max_digits=5, decimal_places=2)
    e = models.FloatField()
    d20_calculated = models.FloatField(max_length=2)
    p_max = models.FloatField()
    pressure = models.FloatField()
    p_unit = models.CharField(max_length=10, choices=UNITS, default='kPa')
    temperature = models.FloatField()
    dp_max = models.FloatField()
    dp_min = models.FloatField()
    dp_unit = models.CharField(max_length=10, choices=UNITS, default='kPa')
    q_max = models.FloatField()
    q_min = models.FloatField()
    betta = models.DecimalField(max_digits=5, decimal_places=5)
    installed_date = models.DateField(null=True, blank=True)
    installed = models.CharField(max_length=15, choices=INSTALLED, default='O`rnatilmagan')
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.meter.object.name} - {self.meter.name} - {self.d20} - {self.number}"