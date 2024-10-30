from django.db import models
from django.utils import timezone

from objects.models import Meter, Organization


class Period(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="period")
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.organization} - {self.date}"


class Volume(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='volumes')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='volumes')
    month = models.DateField(default=timezone.now)
    flowmeter_volume = models.FloatField()
    ns_0 = models.FloatField(default=0)
    ns_1 = models.FloatField(default=0)
    ns_2 = models.FloatField(default=0)
    ns_3 = models.FloatField(default=0)
    ns_4 = models.FloatField(default=0)
    ns_5 = models.FloatField(default=0)
    ns_6 = models.FloatField(default=0)
    ns_7 = models.FloatField(default=0)
    restored_volume = models.FloatField(editable=False)

    class Meta:
        unique_together = ['meter', 'period']

    def save(self, *args, **kwargs):
        # Автоматический расчет restored_volume
        self.restored_volume = (
            self.flowmeter_volume +
            self.ns_0 +
            self.ns_1 +
            self.ns_2 +
            self.ns_3 +
            self.ns_4 +
            self.ns_5 +
            self.ns_6 +
            self.ns_7
        )
        super(Volume, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.meter.object.name} - {self.meter.name} - {self.month.strftime('%B %Y')}"
