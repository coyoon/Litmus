from django.db import models
from django.utils import timezone

class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    hexa = models.CharField(max_length=6)
    rgb_r = models.IntegerField()
    rgb_g = models.IntegerField()
    rgb_b = models.IntegerField()
   
    def _get_rgb_from_hexa(self):
        self.rgb.r=hexa
        self.save()

    def __str__(self):
        return self.name