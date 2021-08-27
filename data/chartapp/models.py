from django.db import models

# Create your models here.
class CounterData(models.Model):
    country = models.CharField(max_length=30)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Country Populaation Data'

    def __str__(self):
        return f'{self.country}--{self.population}'
