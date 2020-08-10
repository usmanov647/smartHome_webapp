from django.db import models

# Create your models here.
class Zone(models.Model):
    zone_name = models.CharField(max_length=5)
    description = models.CharField(max_length=11, default="N/A")
    floor = models.IntegerField(default=1)
    temperature_set = models.IntegerField(default=20)
    temperature_actual = models.DecimalField(decimal_places=1, max_digits=2, default=0.0)
    light_color = models.CharField(max_length=6, default='00FF00')

    def __str__(self):
        return self.zone_name