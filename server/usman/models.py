from django.db import models

# Create your models here.
class Zone(models.Model):
    zone_name = models.CharField(max_length=5)
    description = models.CharField(max_length=11, default="N/A")
    floor = models.IntegerField(default=1)
    zone_temperature = models.IntegerField(default=20)
    zone_light_color = models.CharField(max_length=6, default='00FF00')

    def __str__(self):
        return self.zone_name