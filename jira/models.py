from django.db import models

# Create your models here.

class MonthlyQuickNumber(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    jql = models.TextField()
    url_param = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Monthly Quick Number"
        verbose_name_plural = "Monthly Quick Numbers"
