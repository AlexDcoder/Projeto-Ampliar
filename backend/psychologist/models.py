from django.db import models

# Create your models here.
class Psychologist(models.Model):
    name = models.CharField(max_length=100)
    crp = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
    
