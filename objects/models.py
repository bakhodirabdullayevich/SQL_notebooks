from django.db import models
from django.template.defaultfilters import default


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    e_mail = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class ObjectType(models.Model):
    object_type = models.CharField(max_length=255)

    def __str__(self):
        return self.object_type


class Object(models.Model):
    REGION = (
        ('Qoraqalpog`iston Respublikasi', 'Qoraqalpog`iston Respublikasi'),
        ('Andijon viloyati', 'Andijon viloyati'),
        ('Buxoro viloyati', 'Buxoro viloyati'),
        ('Fargʻona viloyati', 'Fargʻona viloyati'),
        ('Jizzax viloyati', 'Jizzax viloyati'),
        ('Xorazm viloyati', 'Xorazm viloyati'),
        ('Namangan viloyati', 'Namangan viloyati'),
        ('Navoiy viloyati', 'Navoiy viloyati'),
        ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'),
        ('Samarqand viloyati', 'Samarqand viloyati'),
        ('Sirdaryo viloyati', 'Sirdaryo viloyati'),
        ('Surxondaryo viloyati', 'Surxondaryo viloyati'),
        ('Toshkent viloyati', 'Toshkent viloyati'),

    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='object')
    object_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50, choices=REGION)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True, default=0)
    longitude = models.FloatField(null=True, blank=True, default=0)
    year = models.CharField(max_length=4, default=1900, null=True, blank=True)
    power = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class FlowMeterType(models.Model):
    flow_meter_type = models.CharField(max_length=50)
    photo = models.FileField(upload_to='flow_meter_photos', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.flow_meter_type


class Meter(models.Model):

    CONTRACTOR = (
        ('Hududgazta`minot', 'Hududgazta`minot'),
        ('UzGazTrade', 'UzGazTrade'),
        ('O`zneftgaz', 'O`zneftgaz'),
        ('SanEG', 'SanEG'),
        ('Boshqa', 'Boshqa'),

    )
    meter_id = models.CharField(max_length=16)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="meter")
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="meter")
    name = models.CharField(max_length=50)
    diameter = models.DecimalField(max_digits=5, decimal_places=2)
    flow_meter_type = models.ForeignKey(FlowMeterType, on_delete=models.CASCADE)
    flow_meter_serial_number = models.CharField(max_length=50)
    flow_meter_year = models.CharField(max_length=4)
    owner = models.CharField(max_length=50)
    contractor = models.CharField(max_length=50, choices=CONTRACTOR)
    comment = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.object.name} - {self.name}"


class FlowMeterSertificate(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name="sertificate")
    number = models.CharField(max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    url_sertificate = models.FileField(upload_to='sertificates', null=True, blank=True)
    IS_ACTIVE_CHOICES = (
        ('Amalda', 'Amalda'),
        ('Amalda emas', 'Amalda emas'),
    )
    is_active = models.CharField(max_length=20, choices=IS_ACTIVE_CHOICES, default='Amalda')

    def __str__(self):
        return f"{self.meter.name} - Sertifikat raqami {self.number}"

